import datetime
from flask import Flask, render_template, request, json

application = Flask("News")

def getNews():
    resultStr = ''
    with open("news.json", "r", encoding="UTF-8") as f:
        newsList = f.read()
        newsList = json.loads(newsList)
        for news in newsList:
            resultStr += '<div class="content">'
            resultStr += f'<h2>{news["title"]}</h2>'
            resultStr += f'<h5>{news["date"]}</h5>'
            resultStr += f'<div>{news["text"]}</div>'
            resultStr += '</div>'
        f.close()
    return resultStr

def addNews(title: str, text: str):
    currentDate = datetime.datetime.today()
    with open("news.json", "r", encoding="UTF-8") as f:
        newsList = json.loads(f.read())
        newsData = {"title": title, "date": currentDate, "text": text}
        newsList.append(newsData)
        with open("news.json", "w", encoding="UTF-8") as f2:
            f2.write(json.dumps(newsList, indent=2))
            f2.close()
        f.close()

def createDataTable():
    table = "<table id='con_table'>"
    with open("news.json", "r", encoding="UTF-8") as f:
        newsList = f.read()
        newsList = json.loads(newsList)
        index = 0
        for news in newsList:
            table += f'<tr><td><button id="delete" name="delete" value="{index}">X</button></td>'
            table += f'<td>{news["title"]}</td>'
            table += f'<td>{news["date"]}</td>'
            table += '<tr>'
            index += 1
        f.close()
    table += "</table>"
    return table

@application.route("/")
def start():
    content = getNews()
    return render_template("index.html", content=content)

@application.route("/editor")
def editor():
    if request.method == "GET":
        title = request.args.get("title")
        text = request.args.get("text")
        if title != None and text != None:
            addNews(title, text)
    return render_template("editor.html")

@application.route("/admin")
def admin():
    if request.method == "GET":
        index = request.args.get("delete")
        if index != None:
            with open("news.json", "r", encoding="UTF-8") as f:
                newsList = json.loads(f.read())
                del newsList[int(index)]
                with open("news.json", "w", encoding="UTF-8") as f2:
                    f2.write(json.dumps(newsList, indent=2))
                    f2.close()
                f.close()

    table = createDataTable()

    return render_template("admin.html", table=table)

application.run(host="0.0.0.0", port=8081)