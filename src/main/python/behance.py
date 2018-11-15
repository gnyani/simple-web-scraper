import urllib, json

class Behance(object):

    def __init__(self, userName, config):
        self.baseUrl = config.get('BEHANCE','behanceBaseUrl')
        self.accessKey = config.get('BEHANCE','behanceClientId')
        self.userName = userName


    def getBehanceInfoForUser(self):
        print("***********BEHANCE LOGS***************")
        requesturl = self.baseUrl + self.userName + "?client_id=" + self.accessKey
        print("Getting Info from Behance for userName " + self.userName + " from " + requesturl)
        response = urllib.urlopen(requesturl)
        data = json.loads(response.read())
        print "response received is " + str(data)
        requiredinfo = self.parseData(data)
        return requiredinfo

    def parseData(self, data):
        if 'user' in data:
            userinfo = data["user"]
            return userinfo['stats']['followers']
        else:
            return "NotFound"
