import requests
import bs4
from bs4 import BeautifulSoup
import json

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
URL = "https://quatvn.club/"
IMAGE_CLASS=".mace-gallery-teaser"
IMAGE_ATTRIBUTE="data-g1-gallery"

VIDEO_CLASS=".fp-playlist-external"
VIDEO_ATTRIBUTE="data-item"

URL_CLASS="entry-featured-media"

def getSoup(URL):
  resp = requests.get(URL,headers=headers)
  soup = BeautifulSoup(resp.text, 'html.parser')
  return soup

def getImages(soup):
  raw_data=raw_data=soup.select_one(IMAGE_CLASS)
  if not raw_data: return []

  raw_images=raw_data.attrs[IMAGE_ATTRIBUTE]

  if not raw_images: return []

  return json.loads(raw_images)
    
def getVideos(soup):
    raw_data=soup.select_one(VIDEO_CLASS)
    if not raw_data: return []
    videos=[]
    for i in raw_data:
      if type(i) is not bs4.element.NavigableString:
            raw_videos=i.attrs[VIDEO_ATTRIBUTE]
            if not raw_videos: continue
            videos.append(json.loads(raw_videos))
    return videos


def exactData(URL,title):
  soup = getSoup(URL)
  images=getImages(soup)
  videos=getVideos(soup)
  thumbnail=""
  full=""
  if  images: 
      if images[0]["thumbnail"]:
        thumbnail = images[0]["thumbnail"]
      if images[0]["full"]:
        full=images[0]["full"]
  return {
      "title":title,
      "url":URL,
      "images":images,
      "videos":videos,
      "thumbnail":thumbnail,
      "full":full
  }
  
def fetchData(pages=2):
    data =[]
    for i in range(1,pages):
        print(i)
        soup = getSoup("https://quatvn.club/page/{page}".format(page=i))
        raw_data=soup.find_all("div",URL_CLASS)
        if not raw_data:return
        for j in raw_data:
            a_element=j.find("a")

            if not a_element: continue

            title=a_element.attrs["title"]
            link=a_element.attrs["href"]

            if not title or not link: continue

            data.append(exactData(link,title))

    return data

def craw_data():
    print("logs")