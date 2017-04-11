import requests

class RESTClient(object):

    def __init__(self, username=None, password=None):
        self.auth = None
        if username and password:
            self.auth = requests.auth.HTTPBasicAuth(username, password)

        #Default headers type, can be updated, based on provided headers value.
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        self.verify = False

    def get(self, url, headers=None, **kwargs):
        return self.execute('GET', url, headers=headers, **kwargs)

    def post(self, url, headers=None, **kwargs):
        return self.execute("POST", url, headers=headers, **kwargs)

    def execute(self, method, url, headers=None, **kwargs):
        try:
            #Update headers with new header values
            #logging.info("%s request URL: %s", method, url)
            reqheaders = self.headers or {}
            reqheaders.update(headers or {})

            responsdata = requests.request(method, url, headers=reqheaders, auth=self.auth, verify=self.verify,
                                           **kwargs)
            return responsdata

        except Exception as ex:
            raise Exception("Request Exception : %s", ex)
