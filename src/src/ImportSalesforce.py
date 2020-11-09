import pandas as pd
import requests

class SalesForce:
    def __init__(self, params):
        r = requests.post("https://login.salesforce.com/services/oauth2/token", params=params)
        self.access_token = r.json().get("access_token")

    def query(self, instance, query):
        query_url='https://'+instance+'.salesforce.com/services/data/v45.0/queryAll/?q='+query
        headers = {
            'Content-type': 'application/json',
            'Accept-Encoding': 'gzip',
            'Authorization': 'Bearer %s' % self.access_token
        }
        data = requests.get(url=query_url, headers=headers)
        data=data.json()
        sfdf = pd.DataFrame(data['records']).drop(columns='attributes')
        print(sfdf)
