#!/usr/bin/python
# -*- coding: utf-8 -*-

from vale_data_load import DataLoad

datlod = DataLoad()
data_lgs1 = datlod.from_xlxs('../OlahData/LGS_Overall_2017_2023_hourly.xlsx')
datlod.show_data(data_lgs1)
datlod.show_data_header(data_lgs1,'TimeStamp')

