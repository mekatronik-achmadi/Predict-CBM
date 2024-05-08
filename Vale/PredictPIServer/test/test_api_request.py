#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import time

from ValePredictPI.vale_connect import ValeConnect

class TestValeAPI():

    def __init__(self):
        super(TestValeAPI, self).__init__()

        self.server_root = '142.40.33.208'

        self.server_base = 'pti-pi'
        self.x_tag = ['U-LGS1-GB-X-PK-PK-70-AI','U-LGS1-LGB-Y-PK-PK-340-AI',
                      'U-LGS1-TGB-X-PK-PK-270-AI','U-LGS1-TGB-Y-PK-PK-340-AI',
                      'U-LGS1-UGB-X-PK-PK-70-AI','U-LGS1-UGB-Y-PK-PK-340-AI']

        t = time.time()

        self.conn = ValeConnect(self.server_root,self.server_base)

        for i in self.x_tag:
            x_tag_wid = self.conn.get_webid_point(i)
            value_resp = self.conn.get_stream_rec_valuetime_pd(x_tag_wid)

            print(value_resp)
            print(type(value_resp['Timestamps'][1]))
            print(type(value_resp['Values'][1]))

        x_tag_wid = self.conn.get_webid_point(self.x_tag[0])
        time_list = ['2022-01-01 00:00:00','2022-01-01 01:00:00']
        result = self.conn.get_stream_rec_valuetimestamp_pd(x_tag_wid,time_list)
        print(result)

        elapsed = time.time() - t
        print(elapsed)

if __name__ == "__main__":
    vale = TestValeAPI()