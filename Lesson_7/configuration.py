from bs4 import BeautifulSoup
import requests
import zipfile
import os


def getImagesUrl(url: str) -> list:
    urlsList = []
    response = requests.get(url).content
    soup = BeautifulSoup(response, "html.parser")
    for imageLink in soup.findAll("img"):
        urlsList.append(imageLink.get("src"))
    for imageLink in soup.findAll("a"):
        urlsList.append(imageLink.get("href"))
    return urlsList


def downloadImage(url: str) -> str:
    try:
        imageName = f"{url.split('/')[-1]}"
        if not len(imageName.split(".")) < 2:
            imageName.replace("\t", "")
            with open(f"{imageName}", "bw") as imageFile:
                for chunk in requests.get(url, stream=True).iter_content(chunk_size=1024 * 1024):
                    if chunk: imageFile.write(chunk)
                imageFile.close()
                print(f"Image \"{imageName}\" downloaded success!")
            return imageName
        else:
            return "Error"
    except Exception as exception:
        print(exception)
        return "Error"


def createZIPFile(url: str, archiveName: str):
    with zipfile.ZipFile(fr'{archiveName}', 'w') as zipFile:
        for image in getImagesUrl(url):
            imageName = downloadImage(image)
            if imageName == "Error": continue
            if imageName not in zipFile.namelist():
                zipFile.write(imageName)
            os.remove(imageName)
        zipFile.close()
