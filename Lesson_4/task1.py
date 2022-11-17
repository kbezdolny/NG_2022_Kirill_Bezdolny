from get_data import *

commandsList = [["CPU Info", "Name",  "Physical cores", "Logical processors", "Current core frequency"],
                ["RAM Info", "Total Memory Size", "Free memory", "Used memory"],
                ["Swap Memory info", "Total Memory Size", "Free memory", "Used memory"],
                ["Disks Info", "-> Disk Section <-", "Disk fstype", "Total Memory Size", "Free memory", "Used memory"],
                ["Python Info", "Python implementation", "Python version", "Python compiler"],
                ["OC Info", "Network name", "OC Platform", "OC Architecture", "OC Version"],
                ["Network", "-> Interface Section <-", "IP", "Netmask", "Broadcast"]]
additionCommandsList = [["GPU Info", "Name", "Driver version", "Video architecture", "Current refresh rate"]]

keysList = "abcdefghijklmnopqrstuvwxz"

# Get OC Platform type and make finally commands list
ocPlatform = platform.system()
if ocPlatform == "Windows":
    commandsList = additionCommandsList + commandsList
    commandsList[1].insert(2, "Socket")

startManager(commandsList, keysList)