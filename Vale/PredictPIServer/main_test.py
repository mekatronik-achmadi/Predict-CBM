#!/usr/bin/python
# -*- coding: utf-8 -*-

from ValePredictPI.vale_connect import ValeConnect

server_root = '142.40.33.208'
server_base = 'pti-pi'
x_tag = 'U-LGS1-GB-X-PK-PK-70-AI'

conn = ValeConnect(server_root,server_base)

x_tag_wid = conn.get_webid_point(x_tag)
value_array = conn.get_stream_rec_json_value(x_tag_wid)

print(value_array)
print(f"Retrieved Array {value_array.shape}")
print("Tag Web ID: %s" % (x_tag_wid))

