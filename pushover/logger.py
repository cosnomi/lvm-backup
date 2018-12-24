import json
import requests
from .my_config import PUSHOVER_URL, USER_KEY, API_KEY

class PushoverNotification:
    def __init__(self, title):
        self.title = title
    def log(self, mes):
        try:
            payload = {
                'token': API_KEY,
                'user': USER_KEY,
                'title': self.title,
                'message': mes,
                'priority': 0,
            }
            headers = {'content-type': 'application/json'}
            res = requests.post(PUSHOVER_URL, data=json.dumps(payload), headers=headers)
        except Exception as e:
            # ignore exception
            print(e)
    def error(self, mes):
        try:
            payload = {
                'token': API_KEY,
                'user': USER_KEY,
                'title': self.title,
                'message': mes,
                'priority': 2,
                'retry': 1800,
                'expire': 43200
            }
            headers = {'content-type': 'application/json'}
            res = requests.post(PUSHOVER_URL, data=json.dumps(payload), headers=headers)
        except Exception as e:
            # ignore exception
            print(e)