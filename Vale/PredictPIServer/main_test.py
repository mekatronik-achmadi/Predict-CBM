#!/usr/bin/python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from threading import Thread as thd
from time import sleep

from ValePredictPI.vale_connect import ValeConnect

class ValeMain():
    def __init__(self):
        self.server_root = '142.40.33.208'

        self.server_base = 'pti-pi'
        self.x_tag = 'U-LGS1-GB-X-PK-PK-70-AI'

        self.conn = ValeConnect(self.server_root,self.server_base)

        self.x_tag_wid = self.conn.get_webid_point(self.x_tag)
        self.value_array = self.conn.get_stream_rec_json_value(self.x_tag_wid)

        print(self.value_array)
        print(f"Retrieved Array {self.value_array.shape}")
        print("Tag Web ID: %s" % (self.x_tag_wid))

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.x_axis = np.arange(0,len(self.value_array),1)
        self.line, = self.ax.plot(self.x_axis,self.value_array)

        ani = animation.FuncAnimation(fig=self.fig, func=self.granim, interval=0.005,repeat=False)
        ani._start()

        thd(target=self.update_data).start()
        plt.show()

    def granim(self,args):
        self.line.set_data(self.x_axis,self.value_array)

    def update_data(self):
        while True:
            print('Request New Data')
            self.value_array = self.conn.get_stream_rec_json_value(self.x_tag_wid)
            print(self.value_array)
            sleep(1)

if __name__ == "__main__":
    vale = ValeMain()
