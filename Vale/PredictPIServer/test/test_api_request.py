#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import pandas

from ValePredictPI.vale_connect import ValeConnect

class TestValeAPI():

    def __init__(self):
        super(TestValeAPI, self).__init__()

        self.server_root = '142.40.33.208'

        self.server_base = 'pti-pi'
        self.x_tag = 'U-LGS1-GB-X-PK-PK-70-AI'

        self.conn = ValeConnect(self.server_root,self.server_base)

        self.x_tag_wid = self.conn.get_webid_point(self.x_tag)
        self.value_resp = self.conn.get_stream_rec_valuetime(self.x_tag_wid)

        # convert timestamps to pandas
        df = pandas.DataFrame(list(self.value_resp.items()), columns=['Timestamps', 'Values'])
        print(df)
        print(type(df))

if __name__ == "__main__":
    vale = TestValeAPI()