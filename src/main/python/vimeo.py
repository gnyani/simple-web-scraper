import urllib, json

class Vimeo(object):

    def __init__(self, userName, config):
        self.baseUrl = config.get('VIMEO','vimeoBaseUrl')
        self.trailingUrl = config.get('VIMEO','vimeoTrailingUrl')
        self.accessKey = config.get('VIMEO','vimeoAccessToken')
        self.userName = userName


    def getVimeoInfoForUser(self):
        print("***********VIMEO LOGS***************")
        requesturl = self.baseUrl + self.userName + self.trailingUrl + "?access_token=" + self.accessKey
        print("Getting Info from Vimeo for userName " + self.userName + " from " + requesturl)
        response = urllib.urlopen(requesturl)
        data = json.loads(response.read())
        print "response received is " + str(data)
        requiredinfo = self.parseData(data)
        return requiredinfo

    def parseData(self, data):
        if 'total' in data.keys():
            return data['total']
        else:
            return "NotFound"
