# import requests
# from bs4 import BeautifulSoup
#
# class LinkedIn(object):
#
#     def __init__(self, userName, config):
#         self.baseUrl = config.get('LINKEDIN','linkedInBaseUrl')
#         self.userName = userName
#
#
#     def getLinkedInInfoForUser(self):
#         print("***********LINKEDIN LOGS***************")
#         requesturl = self.baseUrl + self.userName
#         print("Getting Info from LinkedIn for userName " + self.userName + " from " + requesturl)
#         response = requests.get(requesturl)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         print "response received is \n" + soup.prettify()
#         requiredinfo = self.parseData(soup)
#         return requiredinfo
#
#     def parseData(self, soup):
#         return 1
#         #follower_count = soup.find('div', attrs={'class':'member-connections'})
#         #print "follower_count element is" + str(follower_count)
#         #return str(follower_count.find('strong').text)
