import requests

class ApiClientConfig:
    def __init__(self, config={}):
        self.config = config

    def get_config(self):
        return self.config
    
    def get(self, key):
        return self.config[key]
    

class ApiClient:
    def __init__(self, config):
        self.config = config

    def post(self, url, body={}):
        auth = self._buildAuthentication()
        requests.post(url, auth=auth, json=body)

    def get(self, url):
        auth = self._buildAuthentication()
        response = requests.get(url, auth=auth)
        return response.json()

    def put(self, url, body={}):
        auth = self._buildAuthentication()
        response = requests.put(url, auth=auth, json=body)

    def _buildAuthentication(self):
        user = self.config.get('user')
        password = self.config.get('password')

        return (user, password) if user and password else None
     