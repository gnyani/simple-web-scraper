import urllib
from bs4 import BeautifulSoup

class Twitter(object):

    def __init__(self, userName, config):
        self.baseUrl = config.get('TWITTER','twitterBaseUrl')
        self.userName = userName


    def getTwitterInfoForUser(self):
        print("***********TWITTER LOGS***************")
        requesturl = self.baseUrl + self.userName
        print("Getting Info from Twitter for userName " + self.userName + " from " + requesturl)
        response = urllib.urlopen(requesturl)
        soup = BeautifulSoup(response, 'html.parser')
        #print "response received is \n" + soup.prettify()
        requiredinfo = self.parseData(soup)
        return requiredinfo

    def parseData(self, soup):
        follower_count = soup.find('a', attrs={'data-nav':'followers'})
        if follower_count is None:
            return "Not Found"
        else:
            print "follower_count element is" + str(follower_count)
            return str(follower_count['title'].split(' ')[0])
