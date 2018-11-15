import urllib, json

class Pinterest(object):

    def __init__(self, userName, config):
        self.baseUrl = config.get('PINTEREST','baseUrl')
        self.trailingUrl = config.get('PINTEREST','trailingUrl')
        self.userName = userName


    def getPinterestInfoForUser(self):
        print("***********PINTEREST LOGS***************")
        requesturl = self.baseUrl + self.userName + self.trailingUrl
        print("Getting Info from pinterest for userName " + self.userName + " from " + requesturl)
        response = urllib.urlopen(requesturl)
        data = json.loads(response.read())
        print "response received is" + str(data)
        requiredinfo = self.parseData(data)
        return requiredinfo

    def parseData(self, data):
        status = data["status"]
        print("status from pinterest url is " + status)
        if (status == "success"):
            return data["data"]["user"]["follower_count"]
        elif (status == "failure"):
            return "NotFound"
