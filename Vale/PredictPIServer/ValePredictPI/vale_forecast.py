# -*- coding: utf-8 -*-

from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import pmdarima as pm
import pandas as pd

## Linear Predictor using ARIMA method
class ValeArima():

    ## Constructor
    def __init__(self):
        super(ValeArima,self).__init__()

    ## Build Forecasting using ARIMA Model
    # @param dataframe Pandas DataFrame from Server
    # @return Plotting parameter as immutable tuple
    def forecast(self,df_data,periods=60):
        arima_model = pm.auto_arima(df_data['Values'],
                                     start_p=1,
                                     start_q=1,
                                     test='adf',
                                     m=12,
                                     d=None,
                                     D=1,
                                     seasonal=True,
                                     trace=False,
                                     error_action='ignore',
                                     suppress_warnings=True,
                                     stepwise=True)

        fitted,confint = arima_model.predict(n_periods=periods,
                                             return_conf_int=True)
        index_of_fc = range(df_data.index[-1], df_data.index[-1] + periods, 1)

        return (fitted,confint,index_of_fc)

    ## Plotting routines
    # @param dataframe Pandas DataFrame from Server
    # @param numpy Fitting array
    # @param numpy Confint array
    # @param numpy Index of Forecasting array
    def plotting(self,df_data,fitted,confint,index_of_fc):
        fitted_series = pd.Series(fitted, index=index_of_fc)
        lower_series = pd.Series(confint[:, 0], index=index_of_fc)
        upper_series = pd.Series(confint[:, 1], index=index_of_fc)

        plt.figure(figsize=(15,7))
        plt.plot(df_data["Values"], color='#1f76b4')
        plt.plot(fitted_series, color='darkgreen')
        plt.fill_between(lower_series.index,
                    lower_series,
                    upper_series,
                    color='k', alpha=.15)

        plt.title("ARIMA - Forecast")
        plt.show()
