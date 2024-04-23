#!/usr/bin/python
# -*- coding: utf-8 -*-

from predict_data.data_load import DataLoad
from predict_data.data_analysis import DataAnalysis

__author__ = 'Achmadi ST MT'
__credits__ = ['M. Ammar Assyraff ST MT', 'Aprianto D. Prasetyo ST MT']
__maintainer__ = 'Achmadi ST MT'
__email__ = 'mekatronik.achmadi@gmail.com'

datlod = DataLoad()
datlys = DataAnalysis()

data_lgs1 = datlod.from_xlxs('../OlahData/LGS_Overall_2017_2023_hourly.xlsx')

datlod.show_data(data_lgs1)
datlod.show_data_header(data_lgs1,'TimeStamp')

datlys.map_corr(data_lgs1)

