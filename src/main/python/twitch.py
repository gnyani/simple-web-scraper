import urllib, json

class Twitch(object):

    def __init__(self, userName, config):
        self.baseUrl = config.get('TWITCH','twitchBaseUrl')
        self.accessKey = config.get('TWITCH','twitchClientId')
        self.userName = userName


    def getTwitchInfoForUser(self):
        print("***********TWITCH LOGS***************")
        requesturl = self.baseUrl + self.userName + "?client_id=" + self.accessKey
        print("Getting Info from Twitch for userName " + self.userName + " from " + requesturl)
        response = urllib.urlopen(requesturl)
        data = json.loads(response.read())
        print "response received is " + str(data)
        requiredinfo = self.parseData(data)
        return requiredinfo

    def parseData(self, data):
        if 'followers' in data:
            return data['followers']
        else:
            return "NotFound"
