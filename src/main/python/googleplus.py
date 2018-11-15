import urllib, json

class GooglePlus(object):

    def __init__(self, userName, config):
        self.baseUrl = config.get('GOOGLEPLUS','googleBaseUrl')
        self.accessKey = config.get('GOOGLEPLUS','googleKey')
        self.userName = userName


    def getGooglePlusInfoForUser(self):
        print("***********GOOGLEPLUS LOGS***************")
        requesturl = self.baseUrl + self.userName + "?key=" + self.accessKey
        print("Getting Info from google plus for userName " + self.userName + " from " + requesturl)
        response = urllib.urlopen(requesturl)
        data = json.loads(response.read())
        print "response received is " + str(data)
        requiredinfo = self.parseData(data)
        return requiredinfo

    def parseData(self, data):
        if 'circledByCount' in data.keys():
            return data['circledByCount']
        else:
            return "NotFound"
