CURRENT_PLUGIN_PREFIX   = "/video/current"
CURRENT_ROOT            = "http://current.com"
CURRENT_VIDEO_DIRECTORY = "http://current.com/items/"

####################################################################################################
def Start():
	Plugin.AddPrefixHandler(CURRENT_PLUGIN_PREFIX, MainMenu, "Current TV", "icon-default.png", "art-default.png")
	MediaContainer.art = R('art-default.png')
	MediaContainer.title1 = 'Current TV'
####################################################################################################
def VideoDirectory(sender, url):
	dir = MediaContainer(title2=sender.itemTitle)
		
	for video in HTML.ElementFromURL(url).xpath("//div[@class='itemListingAsset']"):
		url = video.xpath('a')[0].get('href')
		thumb = video.xpath('a/img')[0].get('src')
		title = video.xpath('a')[0].get('title')
		dir.Append(WebVideoItem(url, title=title, thumb=thumb))
	return dir

####################################################################################################

def MainMenu():
	dir = MediaContainer()
	dir.Append(Function(DirectoryItem(VideoDirectory,	title="Best Of Current TV", thumb=R("icon-default.png")), url="http://current.com/currenttv.htm"))
#	dir.Append(Function(DirectoryItem(VideoDirectory, title="Currency", thumb=R("currency.png")), url="http://current.com/topics/76253832/currency/default/0.htm"))
	dir.Append(Function(DirectoryItem(VideoDirectory, title="Current Edge", thumb=R("currentedge.png")), url="http://current.com/topics/76254312/current_edge/default/0.htm"))
	dir.Append(Function(DirectoryItem(VideoDirectory, title="Current Fix", thumb=R("currentfix.png")), url="http://current.com/topics/76772252/current_fix/default/0.htm"))
	dir.Append(Function(DirectoryItem(VideoDirectory, title="Current Ride", thumb=R("currentride.png")), url="http://current.com/topics/76253932/current_ride/default/0.htm"))
	dir.Append(Function(DirectoryItem(VideoDirectory, title="Current Tech", thumb=R("currenttech.png")), url="http://current.com/topics/76253842/current_tech/default/0.htm"))
	dir.Append(Function(DirectoryItem(VideoDirectory, title="Current Question", thumb=R("currentquestion.png")), url="http://current.com/topics/76254442/current_question/default/0.htm"))
	dir.Append(Function(DirectoryItem(VideoDirectory, title="Current Virals", thumb=R("currentvirals.png")), url="http://current.com/topics/76254682/current_virals/default/0.htm"))
	dir.Append(Function(DirectoryItem(VideoDirectory, title="Daily Fix", thumb=R("dailyfix.png")), url="http://current.com/topics/76254722/daily_fix/default/0.htm"))
	dir.Append(Function(DirectoryItem(VideoDirectory, title="Infomania", thumb=R("infomania.png")), url="http://current.com/topics/76254712/infomania/default/0.htm"))
	dir.Append(Function(DirectoryItem(VideoDirectory, title="Joe Central", thumb=R("joe.png")), url="http://current.com/topics/86547961/joe_central/default/0.htm"))
#	dir.Append(Function(DirectoryItem(VideoDirectory, title="Salon", thumb=R("salon.png")), url="http://current.com/topics/77314621/salon/default/0.htm"))
#	dir.Append(Function(DirectoryItem(VideoDirectory, title="Supernews", thumb=R("supernews.png")), url="http://current.com/topics/76254232/supernews/default/0.htm"))
	dir.Append(Function(DirectoryItem(VideoDirectory, title="Vanguard Journalism", thumb=R("vanguard.png")), url="http://current.com/topics/501/vanguard_journalism/default/0.htm"))
	dir.Append(Function(DirectoryItem(VideoDirectory, title="Viewer Uploads", thumb=R("uploads.png")), url="http://current.com/uploads.htm"))
	return dir
