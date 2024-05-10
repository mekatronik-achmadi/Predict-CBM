# -*- coding: utf-8 -*-

import pmdarima as pm
import pandas as pd

from PyQt5.QtWidgets import QWidget, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import random
import threading

## Linear Predictor using ARIMA method
class ValeArima():

    ## Constructor
    def __init__(self):
        super(ValeArima,self).__init__()
        self.thd_is_run = False

    ## Build Forecasting using ARIMA Model
    # @details It will freeze the GUI if called directly
    # @param dataframe Pandas DataFrame from Server
    def forecast(self,df_data,periods=60):
        # CLI Status
        print('Forecasting')

        # model build
        arima_model = pm.auto_arima(df_data['Values'],
                                     start_p=1,
                                     start_q=1,
                                     test='adf',
                                     m=8,
                                     d=None,
                                     D=1,
                                     seasonal=True,
                                     trace=False,
                                     error_action='ignore',
                                     suppress_warnings=True,
                                     stepwise=True)

        # predict data
        self.fitted,self.confint = arima_model.predict(n_periods=periods,return_conf_int=True)
        self.index_of_fc = range(df_data.index[-1], df_data.index[-1] + periods, 1)

        # update plotting
        fitted_series = pd.Series(self.fitted, index=self.index_of_fc)
        lower_series = pd.Series(self.confint[:, 0], index=self.index_of_fc)
        upper_series = pd.Series(self.confint[:, 1], index=self.index_of_fc)

        self.plt_fig.clear()

        ax = self.plt_fig.add_subplot(111)
        ax.plot(df_data["Values"], color='#1f76b4')
        ax.plot(fitted_series, color='darkgreen')
        ax.fill_between(lower_series.index,
                    lower_series,
                    upper_series,
                    color='k', alpha=.15)

        self.plt_canvas.draw()

        # CLI Status
        print('Forecasted')

        # available for next forecasting
        self.thd_is_run = False

    ## Build Forecasting using ARIMA Model
    # @details It will freeze the GUI if called directly
    # @param dataframe Pandas DataFrame from Server
    def forecast_thd(self,df_data,periods=60):
        if not self.thd_is_run:
            self.thd_is_run = True
            threading.Thread(target=self.forecast, args=(df_data,periods)).start()

    ## Add Plot Widget
    # @return qwidget Plot container as QWidget
    def add_plot(self):
        self.plt_fig = Figure()
        self.plt_canvas = FigureCanvas(self.plt_fig)

        plt_layout = QVBoxLayout()
        plt_layout.addWidget(self.plt_canvas)

        plt_container = QWidget()
        plt_container.setFixedHeight(500)
        plt_container.setFixedWidth(1000)
        plt_container.setLayout(plt_layout)

        return plt_container

    ## Plotting routines
    # @param dataframe Pandas DataFrame from Server
    def plotting(self,df_data):
        fitted_series = pd.Series(self.fitted, index=self.index_of_fc)
        lower_series = pd.Series(self.confint[:, 0], index=self.index_of_fc)
        upper_series = pd.Series(self.confint[:, 1], index=self.index_of_fc)

        self.plt_fig.clear()

        ax = self.plt_fig.add_subplot(111)
        ax.plot(df_data["Values"], color='#1f76b4')
        ax.plot(fitted_series, color='darkgreen')
        ax.fill_between(lower_series.index,
                    lower_series,
                    upper_series,
                    color='k', alpha=.15)

        self.plt_canvas.draw()

    ## Test Plot in slow refresh rate without animation
    def test_plot(self):
        data = [random.random() for i in range(10)]

        self.plt_fig.clear()
        ax = self.plt_fig.add_subplot(111)
        ax.plot(data, '*-')
        self.plt_canvas.draw()
