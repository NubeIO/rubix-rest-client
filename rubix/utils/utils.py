import datetime
import json
import urllib.parse


class Utils:

    @classmethod
    def time_now(cls):
        return datetime.datetime.now()

    @classmethod
    def http_response(cls, res):
        return_dict = {'result': 'success'}
        if res.status_code != 200:
            return_dict['result'] = "failure"
            return_dict['message'] = json.loads(
                res.content
            )['message']
            return return_dict
        else:
            return return_dict

    @classmethod
    def http_response_json(cls, res):
        return_dict = {}
        if res.status_code != 200:
            return_dict['result'] = "failure"
            return_dict['message'] = json.loads(
                res.content
            )['message']
            return return_dict
        else:
            return res.json()

    @classmethod
    def http_response_bool(cls, res):
        return_dict = {'result': 'success'}
        if res.status_code != 200:
            return_dict['result'] = "failure"
            return_dict['message'] = json.loads(
                res.content
            )['message']
            return False
        else:
            return True
