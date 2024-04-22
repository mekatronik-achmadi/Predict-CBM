# -*- coding: utf-8 -*-

import pandas
from pprint import pprint

class DataLoad():

    """ Loading and Parse Data Source"""

    def __init__(self):
        # do nothing for now
        pass

    def from_xlxs(self,path,sheet=0):
        pd_xlxs = pandas.read_excel(path,sheet,engine='openpyxl')
        return pd_xlxs

    def show_data(self,var_in):
        if not isinstance(var_in, pandas.DataFrame):
            print('Data input is not Panda DataFrame')
            return

        print('Data Summary:')
        print(var_in)

        print('Data Frame Header:')
        pprint(var_in.columns.tolist())

    def show_data_header(self,var_in,header_str):
        if not header_str:
            print('Header String Empty')

        if not isinstance(var_in, pandas.DataFrame):
            print('Data input is not Panda DataFrame')
            return

        print('Value of %s:' % (header_str))
        print(var_in[header_str])

