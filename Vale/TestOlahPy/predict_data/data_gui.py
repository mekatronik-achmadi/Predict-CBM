# -*- coding: utf-8 -*-

__author__ = 'Achmadi ST MT'
__credits__ = ['M. Ammar Assyraff ST MT', 'Aprianto D. Prasetyo ST MT']
__maintainer__ = 'Achmadi ST MT'
__email__ = 'mekatronik.achmadi@gmail.com'

import tkinter
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib import style

## GUI for Viewing and Control class
# based on tkinter
class DataGui():

    ## Constructor
    # @param title Main Windows title
    def __init__(self,title='Main Window'):
        super(DataGui, self).__init__()

        self.strTheme = 'elegance'

        self.mainwind = tkinter.Tk()
        self.mainwind.geometry('200x200')
        self.mainwind.title(title)

        theme = ThemedStyle(self.mainwind)
        theme.theme_use(self.strTheme)

    ## Generic TextBox generator
    # @param str_in String to show
    # @param title Window title
    def show_textbox(self,str_in='Empty',title='TextBox'):
        txtwind = tkinter.Toplevel(self.mainwind)
        txtwind.geometry('400x400')
        txtwind.title(title)

        theme = ThemedStyle(txtwind)
        theme.theme_use(self.strTheme)

        txt = tkinter.Text(txtwind,height=300,width=300)
        txt.pack()

        txt.insert(tkinter.END, str_in)

    ## Generic GraphBox generator
    # @param fig Matplotlib Figure object
    # @param title Window title
    def show_graph(self,fig,title='GraphBox'):
        grpwind = tkinter.Toplevel(self.mainwind)
        grpwind.geometry('800x800')
        grpwind.title(title)

        theme = ThemedStyle(grpwind)
        theme.theme_use(self.strTheme)

        style.use('ggplot')
        graphfrm = ttk.Frame(grpwind)

        canvas = FigureCanvasTkAgg(fig,master=graphfrm)
        canvas.draw()
        canvas.get_tk_widget().pack()

        graphfrm.pack()

    ## Run Main Window
    # Also run the Main Loop
    # should called the last
    def run(self):
        self.mainwind.mainloop()

