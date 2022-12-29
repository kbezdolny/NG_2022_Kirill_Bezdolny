from flask import Flask, render_template, redirect, request
from databaseWorker import *
import platform
import psutil

commandsNameList = [["CPU Info", "Cpu Name", "Cpu Physical Cores", "Cpu Logical Processors", "Cpu Current Core Frequency"],
                ["RAM Info", "Total Ram Memory Size", "Free Ram Memory", "Used Ram Memory"],
                ["Swap Memory info", "Total Swap Memory Size", "Free Swap Memory", "Used Swap Memory"],
                ["Disks Info", "Disk Section", "Disk Fstype", "Total Disk Memory Size", "Free Disk Memory", "Used Disk Memory"],
                ["Python Info", "Python Implementation", "Python Version", "Python Compiler"],
                ["OC Info", "Network Name", "OC Platform", "OC Architecture", "OC Version"]]
commandsTagNameList, checkboxStatusList = [], []

# filling "commandsTagNameList" by lower name from "commandsNameList" (for attribute "name" in HTML tag -> "<input/>")
for names in commandsNameList:
    currentNamesList = []
    for name in names:
        currentNamesList.append(name.lower().replace(" ", "_"))
    commandsTagNameList.append(currentNamesList)


# automatically create checkboxes (in HTML format) from input list
def createHTMLCheckboxes(commandsList: list, namesList: list) -> str:
    htmlData = ""
    for paragraphIndex in range(len(commandsList)):
        htmlData += '<div class="paragraphs">'
        htmlData += f'<label class="paragraph">{commandsList[paragraphIndex][0]}' \
                    f'<input type="checkbox" name="{namesList[paragraphIndex][0]}" checked/></label>'
        for underParagraphIndex in range(len(commandsList[paragraphIndex][1:])):
            htmlData += f'<label class="under_paragraphs">{commandsList[paragraphIndex][underParagraphIndex + 1]}' \
                        f'<input type="checkbox" name="{namesList[paragraphIndex][underParagraphIndex + 1]}" checked/></label>'
        htmlData += "</div>"
    return htmlData


# create HTML table with PC Data
def createHTMLDataTable(dataList: list) -> str:
    resultHTML = "<table><tr><td><u>________Data________</u></td><td><u>______________________Value______________________</u></td></tr>"
    for data in dataList:
        for dataKey in data:
            resultHTML += f"<tr><td>{dataKey}</td><td>{data[dataKey]}</td></tr>"
    resultHTML += "<tr><td><u>———————————</u></td><td><u>———————————————————————————</u></td><table/>"
    return resultHTML

# get status from all checkbox (on/off)
def getCheckBoxStatus(namesList: list, statusList: list):
    statusList.clear()
    for paragraphIndex in range(len(namesList)):
        tmpDict = []
        for underParagraphIndex in range(len(namesList[paragraphIndex])):
            paragraph = namesList[paragraphIndex][underParagraphIndex]
            data = request.args.get(paragraph)
            if data == "on":
                tmpDict.append(paragraph)
        statusList.append(tmpDict)


# returned all selected data
def returnDataInformation(namesList: list, checkboxStatus: list, baseName: str):
    dataFunctionsList = [getCPUInfo, getRAMInfo, getSwapMemoryInfo, getDisksInfo, getPythonInfo, getOCInfo]

    # get data from all selected functions and append to result string
    for functionID in range(len(dataFunctionsList)):
        try:
            if namesList[functionID][0] == checkboxStatus[functionID][0]:
                sendDataToDB(getPCData(namesList[functionID][1:], checkboxStatus[functionID][1:], dataFunctionsList[functionID]()), baseName=baseName)
        except Exception as e:
            print(e)


# created string from input list
def sendDataToDB(dataSet: list, baseName: str):
    for currentSet in dataSet:
        for data in currentSet:
            setDataToDB(baseName, data, currentSet[data])


# repetitive actions for each of the "Get PC Data Functions" were placed in one
def getPCData(namesList: list, checkboxStatus: list, dataFunction) -> list:
    commandsList = []
    for iteration in range(len(dataFunction)):
        commandsDict = {}
        for commandID in range(len(namesList)):
            if namesList[commandID] in checkboxStatus:
                commandsDict.setdefault(namesList[commandID], dataFunction[iteration][commandID])
        commandsList.append(commandsDict)
    return commandsList


# =-=-=-=-=-=-=-=-=-= Get PC Data Functions =-=-=-=-=-=-=-=-=-= #

def getCPUInfo() -> list:
    return [[platform.processor(), psutil.cpu_count(logical=False), psutil.cpu_count(logical=True), psutil.cpu_freq().current]]


def getRAMInfo() -> list:
    ramParameters = psutil.virtual_memory()
    return [[round(float(ramParameters.total / 1073741824), 1), round(float(ramParameters.available / 1073741824), 1),
             round(float(ramParameters.used / 1073741824), 1)]]


def getSwapMemoryInfo() -> list:
    swapMemory = psutil.swap_memory()
    return [[round(float(swapMemory.total / 1073741824), 1), round(float(swapMemory.free / 1073741824), 1),
             round(float(swapMemory.used / 1073741824), 1)]]


def getDisksInfo() -> list:
    functionsList = []
    disksPartitions = psutil.disk_partitions()
    for partition in disksPartitions:
        tmpFunctions = [partition.device, partition.fstype]
        try:
            partitionUsages = psutil.disk_usage(partition.mountpoint)
            tmpFunctions.append(round(partitionUsages.total / 1073741824, 1))
            tmpFunctions.append(round(partitionUsages.used / 1073741824, 1))
            tmpFunctions.append(round(partitionUsages.free / 1073741824, 1))
        except:
            tmpFunctions.append("Unknown")
            tmpFunctions.append("Unknown")
            tmpFunctions.append("Unknown")
        functionsList.append(tmpFunctions)

    return functionsList


def getPythonInfo() -> list:
    return [[platform.python_implementation(), platform.python_version(), platform.python_compiler()]]


def getOCInfo() -> list:
    return [[platform.node(), platform.system(), platform.architecture()[0], platform.version()]]


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
