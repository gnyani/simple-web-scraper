import urllib, json

class YouTube(object):

    def __init__(self, userName, config):
        self.baseUrl = config.get('YOUTUBE','youTubeBaseUrl')
        self.accessKey = config.get('YOUTUBE','youTubeKey')
        self.userName = userName


    def getYouTubeInfoForUser(self):
        print("***********YOUTUBE LOGS***************")
        requesturl = self.baseUrl + self.userName + "&key=" + self.accessKey
        print("Getting Info from YouTube for userName " + self.userName + " from " + requesturl)
        response = urllib.urlopen(requesturl)
        data = json.loads(response.read())
        print "response received is " + str(data)
        requiredinfo = self.parseData(data)
        return requiredinfo

    def parseData(self, data):
        items = data["items"]
        if len(items) > 0:
            if 'statistics' in items[0].keys():
               return str(items[0]["statistics"]["subscriberCount"])
            else:
                return "Not Found"
        else:
            return "NotFound"
