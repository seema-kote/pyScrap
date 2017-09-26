import requests
from bs4 import BeautifulSoup
import re

def scrap(Url):
    rawData = requests.get(Url)
    soup = BeautifulSoup(rawData.content,"html.parser")
    return soup

def drinkSoup(fileName,data):
    file=open(fileName,'w')
    file.write(str(data))
    file.close()

def getTitles(soup):
    result=list()
    titles = soup.findAll("h1",{"class":"entry-title"})
    for title in titles:
        title=BeautifulSoup(str(title),"html.parser")
        title=re.sub(r'[^\x00-\x7F]+', ' ',title.findAll("a")[0].get_text())
        print title
        result.append(title)
    return result

def getText(soup):
    result= list()
    paras = soup.findAll("div",{"class":"entry-summary"})
    for para in paras:
        para=BeautifulSoup(str(para.findAll("p")[0]),"html.parser").get_text()
        result.append(re.sub(r'[^\x00-\x7F]+', ' ',para))
    return result