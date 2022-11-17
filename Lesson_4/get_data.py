# pip install --upgrade wmi
# pip install --upgrade pywin32
# WMI lib only for Windows

import platform
import psutil
import wmi

def enterCommandKey(text: str):
    keysStats =  input(text).split(" ")
    for stat in range(len(keysStats)):
        if keysStats[stat] == "": del keysStats[stat]

    return keysStats


def setKeysStatus(commandsList: list, keysList: str or list):
    keysStatusDict = {}
    for commandIndex in range(len(commandsList)):
        tmpList = ["on"]
        keysStatusDict.setdefault(keysList[commandIndex], tmpList)
        for underKey in range(len(commandsList[commandIndex][1:])):
            tmpList.append("on")

        keysStatusDict[keysList[commandIndex]] = tmpList

    return keysStatusDict


# on or off commands function
def checkboxMenu(key, keysDict: dict):
    if key[0] not in keysDict: return

    # checkbox menu for under keys
    if len(key) == 3 and key[1] != "0":
        if key[2] == "off":
            keysDict[key[0]][int(key[1])] = "off"
        elif key[2] == "on":
            keysDict[key[0]][int(key[1])] = "on"

    # checkbox menu for upper keys
    if len(key) == 2:
        if key[1] == "off":
            keysDict[key[0]][0] = "off"
        elif key[1] == "on":
            keysDict[key[0]][0] = "on"


# returned all selected data
def returnDataInformation(keys: list, ocSystem: str):
    commandsFunctions = [getGPUInfo, getCPUInfo, getRAMInfo, getSwapMemoryInfo, getDisksInfo, getPythonInfo, getOCInfo, getNetworkInfo]

    # deleted getGPUInfo() for others OC System
    if ocSystem != "Windows":
        del commandsFunctions[0]

    # get data from all selected functions and append to result string
    resultInfoString = ""
    for i in range(len(commandsFunctions)):
        if 0 == keys[i][0]:
            resultInfoString += unpackedData(commandsFunctions[i](keys[i]), "") + "\n"

    return resultInfoString


# unpacked the data function
def unpackedData(data: list, operator: str):
    dataString = ""
    for dataIndex in range(len(data)):
        dataString += operator + data[dataIndex] + "\n"

    return dataString


# unpacked under the data function
def unpackedCommandData(keys: list, dataList: list, commandsList: list):
    for currentData in commandsList:
        for commandIndex in range(len(currentData)):
            if commandIndex+1 in keys:
                try: dataList.append(currentData[commandIndex])
                except: continue

    return dataList


def getMenuStatus(key, keysStatus: dict, keysList: str or list):
    # if input key == Y -> get all data from selected commands
    if key[0] in ["y", "Y"]:
        # get all keys where value == "on"
        keysIndexList = []
        for keyIndex in range(len(keysStatus)):
            tmpList = []
            for underKey in range(len(keysStatus[keysList[keyIndex]])):
                if keysStatus[keysList[keyIndex]][underKey] == "on": tmpList.append(underKey)
            keysIndexList.append(tmpList)

        # open and write data to file
        file = open("out_system_properties.txt", "w")
        if file:
            if file.write(returnDataInformation(keysIndexList, platform.system())): print("Deriving properties successfully!")
            file.close()

        return 1

    # else call checkboxMenu() function
    elif key[0] in keysStatus and key[1] in "0123456789" and key[2] in ["off", "on"] or \
        key[0] in keysStatus and key[1] in ["on", "off"]:

        checkboxMenu(key, keysStatus)
        return 0


def startManager(commandsList: list, keysList: str or list):
    keysStatusDict = setKeysStatus(commandsList, keysList)
    while True:
        print(">-----------> MENU <-----------<")
        # output commands list
        for commandIndex in range(len(commandsList)):
            print(f"{keysList[commandIndex]}) {commandsList[commandIndex][0]} [{keysStatusDict[keysList[commandIndex]][0]}]")

            for underKey in range(len(commandsList[commandIndex][1:])):
                print(f"\t{underKey+1}) {commandsList[commandIndex][underKey+1]} [{keysStatusDict[keysList[commandIndex]][underKey+1]}]")
        print("Apply and output properties (y/Y)")

        # get menu status
        result = getMenuStatus(enterCommandKey("Enter command: "), keysStatusDict, keysList)
        if result == 1: break

#=================== Get Data Functions =========================#

def getGPUInfo(keys: list):
    gpuData = ["-----------> GPU <-----------"]
    gpuInfo = wmi.WMI().Win32_VideoController()[0]
    commandsList = [[f"Name: {gpuInfo.Name}", f"Driver version: {gpuInfo.DriverVersion}",
                    f"Video architecture: {gpuInfo.VideoArchitecture}",
                    f"Current refresh rate: {gpuInfo.CurrentRefreshRate}"]]

    return unpackedCommandData(keys, gpuData, commandsList)


def getCPUInfo(keys: list):
    cpuData = ["-----------> CPU <-----------"]

    if platform.system() == "Windows":
        processorParametrs = wmi.WMI().Win32_Processor()[0]
        commandsList = [[f"Name: {processorParametrs.Name}", f"Socket: {processorParametrs.SocketDesignation}",
                        f"Physical cores: {processorParametrs.NumberOfCores}",
                        f"Logical processors: {processorParametrs.NumberOfLogicalProcessors}",
                        f"Current core frequency: {processorParametrs.CurrentClockSpeed} MHz"]]
    else:
        commandsList = [[f"Name: {platform.processor()}", f"Physical cores: {psutil.cpu_count(logical=False)}",
                        f"Logical processors: {psutil.cpu_count(logical=True)}",
                        f"Current core frequency: {psutil.cpu_freq().current} MHz"]]

    return unpackedCommandData(keys, cpuData, commandsList)


def getRAMInfo(keys: list):
    ramData = ["-----------> RAM <-----------"]
    ramParametrs = psutil.virtual_memory()
    commandsList = [[f"Total Memory Size: { round(float(ramParametrs.total / 1073741824), 1) } Gb",
                    f"Free memory: { round(float(ramParametrs.available / 1073741824), 1) } Gb",
                    f"Used memory: { round(float(ramParametrs.used / 1073741824), 1) } Gb"]]

    return unpackedCommandData(keys, ramData, commandsList)


def getSwapMemoryInfo(keys: list):
    memoryData = ["-----------> Swap Memory <-----------"]
    swapMemory = psutil.swap_memory()
    commandsList = [[f"Total Memory Size: { round(float(swapMemory.total / 1073741824), 1) } Gb",
                        f"Free memory: { round(float(swapMemory.free / 1073741824), 1) } Gb",
                        f"Used memory: { round(float(swapMemory.used / 1073741824), 1) } Gb"]]

    return unpackedCommandData(keys, memoryData, commandsList)


def getDisksInfo(keys: list):
    disksData = ["-----------> Disks <-----------"]
    commandsList = []
    disksPartitions = psutil.disk_partitions()

    for partition in disksPartitions:
        tmpData = []

        tmpData.append(f"-> Disk {partition.device} <-")
        tmpData.append(f"Disk fstype: {partition.fstype}")
        try:
            partitionUsages = psutil.disk_usage(partition.mountpoint)
            tmpData.append(f"Total Memory Size: {round(partitionUsages.total / 1073741824, 1)} Gb")
            tmpData.append(f"Free memory: {round(partitionUsages.used / 1073741824, 1)} Gb")
            tmpData.append(f"Used memory: {round(partitionUsages.free / 1073741824, 1)} Gb")
        except:
            tmpData.append(f"Total Memory Size: Unknown")
            tmpData.append(f"Free memory: Unknown")
            tmpData.append(f"Used memory: Unknown")
        commandsList.append(tmpData)

    return unpackedCommandData(keys, disksData, commandsList)


def getPythonInfo(keys: list):
    pythonData = ["-----------> Python <-----------"]
    commandsList = [[f"Python implementation: {platform.python_implementation()}",
                    f"Python version: {platform.python_version()}",
                    f"Python compiler: {platform.python_compiler()}"]]

    return unpackedCommandData(keys, pythonData, commandsList)


def getOCInfo(keys: list):
    ocData = ["-----------> OC <-----------"]
    commandsList = [[f"Network name:{platform.node()}", f"Platform: {platform.system()}",
                    f"Architecture: {platform.architecture()[0]}", f"Version: {platform.version()}"]]

    return unpackedCommandData(keys, ocData, commandsList)


def getNetworkInfo(keys: list):
    networkData = ["-----------> Network <-----------"]
    commandsList = []
    ifAddress = psutil.net_if_addrs()

    for interfaceName, interfaceAddresses in ifAddress.items():
        tmpData = []

        tmpData.append(f"-> Interface {interfaceName} <-")
        for address in interfaceAddresses:
            if str(address.family) == "AddressFamily.AF_INET":
                tmpData.append(f"IP: {address.address}")
                tmpData.append(f"Netmask: {address.netmask}")
                tmpData.append(f"Broadcast IP-Address: {address.broadcast}")
            if str(address.family) == "AddressFamily.AF_PACKET":
                tmpData.append(f"MAC-Address: {address.address}")
                tmpData.append(f"Netmask: {address.netmask}")
                tmpData.append(f"Broadcast MAC: {address.broadcast}")
        commandsList.append(tmpData)

    return unpackedCommandData(keys, networkData, commandsList)

#================================================================#