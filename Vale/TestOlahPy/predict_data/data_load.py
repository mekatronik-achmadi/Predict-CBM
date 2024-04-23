# -*- coding: utf-8 -*-

__author__ = 'Achmadi ST MT'
__credits__ = ['M. Ammar Assyraff ST MT', 'Aprianto D. Prasetyo ST MT']
__maintainer__ = 'Achmadi ST MT'
__email__ = 'mekatronik.achmadi@gmail.com'

import pandas

class DataLoad():

    def __init__(self):
        super(DataLoad, self).__init__()

    def from_xlxs(self,path,sheet='',engine='openpyxl'):
        if len(sheet)==0:
            pd_xlxs = pandas.read_excel(path,engine=engine)
        else:
            pd_xlxs = pandas.read_excel(path,sheet_name=sheet,engine=engine)

        pd_xlxs.dropna(axis=0)
        pd_xlxs.dropna(axis=1)

        return pd_xlxs

    def get_header(self,var_in):
        if not isinstance(var_in, pandas.DataFrame):
            print('Data input is not Panda DataFrame')
            return

        collist = var_in.columns.tolist()
        strlist = ''.join(str(element)+'\n' for element in collist)
        return strlist

    def summary_all(self,var_in):
        if not isinstance(var_in, pandas.DataFrame):
            print('Data input is not Panda DataFrame')
            return

        print('Data Summary:')
        print(var_in)

    def summary_by_header(self,var_in,header_str):
        if len(header_str)==0:
            print('Header String Empty')

        if not isinstance(var_in, pandas.DataFrame):
            print('Data input is not Panda DataFrame')
            return

        print('Value of %s:' % (header_str))
        print(var_in[header_str])

