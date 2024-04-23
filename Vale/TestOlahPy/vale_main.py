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
datgui = DataGui()

data_lgs1 = datlod.from_xlxs('../OlahData/LGS_Overall_2017_2023_hourly.xlsx')

datlod.show_data(data_lgs1)
datlod.show_data_header(data_lgs1,'TimeStamp')

datgui.show_graph(datlys.fig_map_corr(data_lgs1))
datgui.show_textbox(datlod.get_header(data_lgs1))
datgui.show_all()
