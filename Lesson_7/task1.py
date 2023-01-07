from flask import Flask, render_template, request, redirect, send_file
from configuration import *
import threading

# URLs for testing:
# https://www.vecteezy.com/photo/712425-california-state-capitol-museum
# https://www.lifeofpix.com/
# https://getrefe.tumblr.com/
# https://nos.twnsnd.co/


application = Flask("Grabber Photos")
archiveName = "photos.zip"


@application.route("/")
def startApplication():
    return render_template("index.html", zipURL=f"<a href='{archiveName}'>Click to download a ZIP file</a>")


@application.route("/grab")
def grabPhotos():
    thread = threading.Thread(target=createZIPFile, args=(request.args.get("url_string"), archiveName))
    thread.start()
    thread.join()
    return redirect("/")


@application.route(f"/{archiveName}")
def downloadArchive():
    try:
        return send_file(f"{archiveName}")
    except:
        return redirect("/")


application.run(host="0.0.0.0", port=8081)
