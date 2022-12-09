import datetime
from flask import Flask, render_template, request, json

application = Flask("News")

def getNews():
    resultStr = ''
    with open("news.json", "r", encoding="UTF-8") as file:
        newsList = file.read()
        newsList = json.loads(newsList)
        for news in newsList:
            resultStr += '<div class="content">'
            resultStr += f'<h2>{news["title"]}</h2>'
            resultStr += f'<h5>{news["date"]}</h5>'
            resultStr += f'<div>{news["text"]}</div>'
            resultStr += '</div>'
        file.close()
    return resultStr

def addNews(title: str, text: str):
    currentDate = datetime.datetime.today()
    with open("news.json", "r", encoding="UTF-8") as file:
        newsList = json.loads(file.read())
        newsData = {"title": title, "date": currentDate, "text": text}
        newsList.append(newsData)
        with open("news.json", "w", encoding="UTF-8") as file2:
            file2.write(json.dumps(newsList, indent=2))
            file2.close()
        file.close()

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

application.run(host="0.0.0.0", port=8081)