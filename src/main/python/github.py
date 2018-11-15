import requests
from bs4 import BeautifulSoup

class Github(object):

    def __init__(self, userName, config):
        self.baseUrl = config.get('GITHUB','gitHubBaseUrl')
        self.userName = userName


    def getGitHubInfoForUser(self):
        print("***********GITHUB LOGS***************")

        requesturl = self.baseUrl + self.userName
        print("Getting Info from Github for userName " + self.userName + " from " + requesturl)
        response = requests.get(requesturl)
        soup = BeautifulSoup(response.text, 'html.parser')
        requiredinfo = self.parseData(soup)
        return requiredinfo

    def parseData(self, soup):
        follower_count = soup.find('a', attrs={'href': '/'+self.userName+'?tab=followers'})
        if follower_count is None:
            return "Not Found"
        else:
            print "follower_count element is" + str(follower_count)
            final_count = follower_count.find('span', attrs={'class':'Counter'}).text
            return str(final_count.strip(' \n\t'))