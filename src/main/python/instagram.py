import urllib
from bs4 import BeautifulSoup

class Instagram(object):

    def __init__(self, userName, config):
        self.baseUrl = config.get('INSTAGRAM','instaBaseUrl')
        self.userName = userName


    def getInstagramInfoForUser(self):
        print("***********INSTAGRAM LOGS***************")
        requesturl = self.baseUrl + self.userName
        print("Getting Info from Instagram for userName " + self.userName + " from " + requesturl)
        response = urllib.urlopen(requesturl)
        soup = BeautifulSoup(response, 'html.parser')
        #print "response received is \n" + soup.prettify()
        requiredinfo = self.parseData(soup)
        return requiredinfo

    def parseData(self, soup):
        follower_count = soup.find('meta', attrs={'name':'description'})
        if follower_count is None:
            return "Not Found"
        else:
           print "follower_count element is" + str(follower_count)
           return str(follower_count['content'].split(',')[0].split(' ')[0])
