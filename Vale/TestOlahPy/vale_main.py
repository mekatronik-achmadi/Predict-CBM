#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Achmadi ST MT'
__credits__ = ['M. Ammar Assyraff ST MT', 'Aprianto D. Prasetyo ST MT']
__maintainer__ = 'Achmadi ST MT'
__email__ = 'mekatronik.achmadi@gmail.com'

from predict_data.data_load import DataLoad
from predict_data.data_analysis import DataAnalysis
from predict_data.data_gui import DataGui

datlod = DataLoad()
datlys = DataAnalysis()
datgui = DataGui('Vale Data Example')

data_lgs1 = datlod.from_xlxs('../OlahData/LGS_Overall_2017_2023_hourly.xlsx')

datlod.summary_all(data_lgs1)
datlod.summary_by_header(data_lgs1,'TimeStamp')

datgui.show_graph(datlys.fig_map_corr(data_lgs1),'Correlation Map')
datgui.show_textbox(datlod.get_header(data_lgs1),'Header List')
datgui.run()

