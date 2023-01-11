# Runs the bot

from instagrapi import Client
import PicManager

# script to add all images in images directory into a .txt file
pm = PicManager.PicManager("/Users/stephanieran/chibi-luffy/picList.txt")
directory = "/Users/stephanieran/chibi-luffy/RedditImageScraper/images"


pm.getList()
pics = pm.getPics(3)
pm.resizePics("/Users/stephanieran/chibi-luffy/RedditImageScraper/images")
pm.rewriteFile() # gets rid of previously posted photos

bot = Client()
bot.login("username", "password") # replace with login credentials

album_path = pics
text =  "#onepiece #anime #animememes #luffy #funnyanimememes #funnymemes #memes #weebs #spyxfamily #otaku"

bot.album_upload(
    album_path,
    caption = text
)