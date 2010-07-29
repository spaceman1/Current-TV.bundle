import re, sys
from PMS import Plugin, Log, DB, Thread, XML, HTTP, JSON, RSS, Utils
from PMS.MediaXML import MediaContainer, DirectoryItem, WebVideoItem, SearchDirectoryItem
from PMS.Shorthand import _L, _R

CURRENT_PLUGIN_PREFIX   = "/video/current"
CURRENT_ROOT            = "http://current.com"
CURRENT_VIDEO_DIRECTORY = "http://current.com/items/"
CURRENT_VIDEO_BESTOF     = "http://current.com/currenttv.htm"
CURRENT_VIDEO_INFOMANIA     = "http://current.com/topics/76254712/infomania/default/0.htm"
CURRENT_VIDEO_SUPERNEWS     = "http://current.com/topics/76254232/supernews/default/0.htm"
CURRENT_VIDEO_CURRENTFIX     = "http://current.com/topics/76772252/current_fix/default/0.htm"
CURRENT_VIDEO_DAILYFIX     = "http://current.com/topics/76254722/daily_fix/default/0.htm"
CURRENT_VIDEO_SALON     = "http://current.com/topics/77314621/salon/default/0.htm"
CURRENT_VIDEO_VIRALS     = "http://current.com/topics/76254682/current_virals/default/0.htm"
CURRENT_VIDEO_JOE     = "http://current.com/topics/86547961/joe_central/default/0.htm"
CURRENT_VIDEO_VANGUARD     = "http://current.com/topics/501/vanguard_journalism/default/0.htm"
CURRENT_VIDEO_QUESTION     = "http://current.com/topics/76254442/current_question/default/0.htm"
CURRENT_VIDEO_TECH     = "http://current.com/topics/76253842/current_tech/default/0.htm"
CURRENT_VIDEO_RIDE     = "http://current.com/topics/76253932/current_ride/default/0.htm"
CURRENT_VIDEO_UPLOADS     = "http://current.com/uploads.htm"
CURRENT_VIDEO_EDGE     = "http://current.com/topics/76254312/current_edge/default/0.htm"
CURRENT_VIDEO_CURRENCY     = "http://current.com/topics/76253832/currency/default/0.htm"

####################################################################################################
def Start():
  Plugin.AddRequestHandler(CURRENT_PLUGIN_PREFIX, HandleVideosRequest, "Current TV", "icon-default.png", "art-default.png")
  Plugin.ExposeResource("logo.png", "image/png")
  Plugin.ExposeResource("art-default.png", "image/jpg")
  
####################################################################################################
def SendVideoDirectory(url, name):
  dir = MediaContainer("art-default.png", None, "Current TV", name)
    
  for video in XML.ElementFromURL(url, True).xpath("//div[@class='itemListingAsset']"):
    url = video.xpath('a')[0].get('href')
    thumb = video.xpath('a/img')[0].get('src')
    title = video.xpath('a')[0].get('title')
    dir.AppendItem(WebVideoItem(url, title, '', '', thumb))
  return dir.ToXML()

####################################################################################################
def HandleVideosRequest(pathNouns, count):
  dir = MediaContainer("art-default.png", None, "Current TV")
  
  if count == 0:
    dir.AppendItem(DirectoryItem("bestof", "Best Of Current TV", _R("icon-default.png")))
    dir.AppendItem(DirectoryItem("currency", "Currency", _R("currency.png")))
    dir.AppendItem(DirectoryItem("edge", "Current Edge", _R("currentedge.png")))
    dir.AppendItem(DirectoryItem("currentfix", "Current Fix", _R("currentfix.png")))
    dir.AppendItem(DirectoryItem("ride", "Current Ride", _R("currentride.png")))
    dir.AppendItem(DirectoryItem("tech", "Current Tech", _R("currenttech.png")))
    dir.AppendItem(DirectoryItem("question", "Current Question", _R("currentquestion.png")))
    dir.AppendItem(DirectoryItem("virals", "Current Virals", _R("currentvirals.png")))
    dir.AppendItem(DirectoryItem("dailyfix", "Daily Fix", _R("dailyfix.png")))
    dir.AppendItem(DirectoryItem("infomania", "Infomania", _R("infomania.png")))
    dir.AppendItem(DirectoryItem("joe", "Joe Central", _R("joe.png")))
    dir.AppendItem(DirectoryItem("salon", "Salon", _R("salon.png")))
    dir.AppendItem(DirectoryItem("supernews", "Supernews", _R("supernews.png")))
    dir.AppendItem(DirectoryItem("vanguard", "Vanguard Journalism", _R("vanguard.png")))
    dir.AppendItem(DirectoryItem("uploads", "Viewer Uploads", _R("uploads.png")))
    return dir.ToXML()
  
  elif pathNouns[0] == 'bestof':
    return SendVideoDirectory(CURRENT_VIDEO_BESTOF, "Best Of Current TV")
  elif pathNouns[0] == 'infomania':
    return SendVideoDirectory(CURRENT_VIDEO_INFOMANIA, "Infomania")
  elif pathNouns[0] == 'supernews':
    return SendVideoDirectory(CURRENT_VIDEO_SUPERNEWS, "Supernews")
  elif pathNouns[0] == 'currentfix':
    return SendVideoDirectory(CURRENT_VIDEO_CURRENTFIX, "Current Fix")
  elif pathNouns[0] == 'dailyfix':
    return SendVideoDirectory(CURRENT_VIDEO_DAILYFIX, "Daily Fix")
  elif pathNouns[0] == 'salon':
    return SendVideoDirectory(CURRENT_VIDEO_SALON, "Salon")
  elif pathNouns[0] == 'virals':
    return SendVideoDirectory(CURRENT_VIDEO_VIRALS, "Current Virals")
  elif pathNouns[0] == 'joe':
    return SendVideoDirectory(CURRENT_VIDEO_JOE, "Joe Central")
  elif pathNouns[0] == 'vanguard':
    return SendVideoDirectory(CURRENT_VIDEO_VANGUARD, "Vanguard Journalism")
  elif pathNouns[0] == 'question':
    return SendVideoDirectory(CURRENT_VIDEO_QUESTION, "Current Question")
  elif pathNouns[0] == 'tech':
    return SendVideoDirectory(CURRENT_VIDEO_TECH, "Current Tech")
  elif pathNouns[0] == 'ride':
    return SendVideoDirectory(CURRENT_VIDEO_RIDE, "Current Ride")
  elif pathNouns[0] == 'uploads':
    return SendVideoDirectory(CURRENT_VIDEO_UPLOADS, "Viewer Uploads")
  elif pathNouns[0] == 'edge':
    return SendVideoDirectory(CURRENT_VIDEO_EDGE, "Current Edge")
  elif pathNouns[0] == 'currency':
    return SendVideoDirectory(CURRENT_VIDEO_CURRENCY, "Currency")