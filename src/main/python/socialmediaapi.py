import ConfigParser
import pprint
from pinterest import Pinterest
from googleplus import GooglePlus
from youtube import YouTube
from twitch import Twitch
from vimeo import Vimeo
from behance import Behance
from instagram import Instagram
from twitter import Twitter
from github import Github

class SocialMediaApi(object):

    def __init__(self, username):
        config = ConfigParser.ConfigParser()
        config.read('./config.properties')
        self.pinterest = Pinterest(username, config)
        self.googleplus = GooglePlus(username, config)
        self.youtube = YouTube(username, config)
        self.twitch = Twitch(username, config)
        self.vimeo = Vimeo(username, config)
        self.behance = Behance(username, config)
        self.instagram = Instagram(username, config)
        self.twitter = Twitter(username, config)
        self.github = Github(username, config)
        self.dict = dict()


    def getAllInfo(self):
        pinterestcount = self.pinterest.getPinterestInfoForUser()
        googlepluscount = self.googleplus.getGooglePlusInfoForUser()
        youtubecount = self.youtube.getYouTubeInfoForUser()
        twitchcount = self.twitch.getTwitchInfoForUser()
        vimeocount = self.vimeo.getVimeoInfoForUser()
        behancecount = self.behance.getBehanceInfoForUser()
        instagramcount = self.instagram.getInstagramInfoForUser()
        twittercount = self.twitter.getTwitterInfoForUser()
        githubcount = self.github.getGitHubInfoForUser()
        self.dict['GITHUB'] = githubcount
        self.dict['TWITTER'] = twittercount
        self.dict['INSTAGRAM'] = instagramcount
        self.dict['BEHANCE'] = behancecount
        self.dict['PINTEREST'] = pinterestcount
        self.dict['GOOGLEPLUS'] = googlepluscount
        self.dict['YOUTUBE'] = youtubecount
        self.dict['TWITCH'] = twitchcount
        self.dict['VIMEO'] = vimeocount

    def printDict(self):
        print ("\n ********Output********* \n")
        pprint.pprint(self.dict)



def main():
    userInput = raw_input("Enter the user name for which you want the info? \n")
    socialMediaApi = SocialMediaApi(userInput)
    socialMediaApi.getAllInfo()
    socialMediaApi.printDict()
if __name__ == "__main__":
    main()