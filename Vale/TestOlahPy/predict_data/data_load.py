# -*- coding: utf-8 -*-

__author__ = 'Achmadi ST MT'
__credits__ = ['M. Ammar Assyraff ST MT', 'Aprianto D. Prasetyo ST MT']
__maintainer__ = 'Achmadi ST MT'
__email__ = 'mekatronik.achmadi@gmail.com'

import pandas

## Data Loading and Pre-Processing class
class DataLoad():

    ## Constructor
    def __init__(self):
        super(DataLoad, self).__init__()

    ## Import from XLSX
    # @param path Excel file path
    # @param sheet Sheet name (optional)
    # @param engine Engine name (optional)
    # @return Pandas DataFrame
    def from_xlsx(self,path,sheet='',engine='openpyxl'):
        if len(sheet)==0:
            pd_xlsx = pandas.read_excel(path,engine=engine)
        else:
            pd_xlsx = pandas.read_excel(path,sheet_name=sheet,engine=engine)

        pd_xlsx.dropna(axis=0)
        pd_xlsx.dropna(axis=1)

        return pd_xlxs

    ## Get Header List string
    # @param var_in Pandas DataFrame
    # @return String
    def get_header(self,var_in):
        if not isinstance(var_in, pandas.DataFrame):
            print('Data input is not Panda DataFrame')
            return

        collist = var_in.columns.tolist()
        strlist = ''.join(str(element)+'\n' for element in collist)
        return strlist

    ## Show Summary in CLI
    # @param var_in Pandas DataFrame
    def summary_all(self,var_in):
        if not isinstance(var_in, pandas.DataFrame):
            print('Data input is not Panda DataFrame')
            return

        print('Data Summary:')
        print(var_in)

    ## Show Summary in CLI on selected column
    # @param var_in Pandas DataFrame
    def summary_by_header(self,var_in,header_str):
        if len(header_str)==0:
            print('Header String Empty')

        if not isinstance(var_in, pandas.DataFrame):
            print('Data input is not Panda DataFrame')
            return

        print('Value of %s:' % (header_str))
        print(var_in[header_str])

