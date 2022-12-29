from configuration import *

application = Flask("Get Computer Data")
baseName = "PCData.db"
prepareDB(baseName)

@application.route("/")
def startApplication():
    return render_template("index.html", data=createHTMLCheckboxes(commandsNameList, commandsTagNameList),
                           table=createHTMLDataTable(getDataFromDB(baseName)))

@application.route("/setdata")
def setData():
    getCheckBoxStatus(commandsTagNameList, checkboxStatusList)
    clearDataInDB(baseName=baseName)
    returnDataInformation(commandsTagNameList, checkboxStatusList, baseName=baseName)
    return redirect("/")

application.run(host="0.0.0.0", port=8081)