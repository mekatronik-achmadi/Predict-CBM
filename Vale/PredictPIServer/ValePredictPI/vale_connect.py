# -*- coding: utf-8 -*-

import requests
from datetime import datetime, timezone
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import json
import urllib3
import numpy

class ValeConnect():

    # Constructor
    def __init__(self,server_path,base_path):
        # no need for super init

        self.SERV_PATH = f'https://{server_path}/piwebapi/'
        self.BASE_PATH = base_path

        # disable SSL warnings
        urllib3.disable_warnings()

    def api_get_request(self,get_url,key=''):
        resp = requests.get(get_url,verify=False)
        resp_json = resp.json()

        if len(key) == 0:
            return resp_json
        else:
            return resp_json[key]

    def get_webid_point(self,tag_path):
        url = f'{self.SERV_PATH}/points?path=\\\\{self.BASE_PATH}\{tag_path}'
        return self.api_get_request(url,'WebId')

    def get_stream_rec_json(self,web_id):
        url = f'{self.SERV_PATH}/streams/{web_id}/recorded'
        return self.api_get_request(url)

    def get_stream_rec_json_value(self,web_id):
        url = f'{self.SERV_PATH}/streams/{web_id}/recorded?selectedFields=Items.Value'
        val_list = self.api_get_request(url,'Items')
        val_np = numpy.zeros((len(val_list)))
        j = 0
        for i in val_list:
            val_np[j] = i.get('Value')
            j = j + 1

        return val_np

