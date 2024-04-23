# -*- coding: utf-8 -*-

__author__ = 'Achmadi ST MT'
__credits__ = ['M. Ammar Assyraff ST MT', 'Aprianto D. Prasetyo ST MT']
__maintainer__ = 'Achmadi ST MT'
__email__ = 'mekatronik.achmadi@gmail.com'

import tkinter
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle

class DataGui():

    def __init__(self):
        super(DataGui, self).__init__()
        self.strTheme = 'elegance'

    def show_textbox(self,str_in='Empty',title='TextBox',clr='yellow'):
        wind = tkinter.Tk()
        wind.geometry('400x400')
        wind.title(title)

        theme = ThemedStyle(wind)
        theme.theme_use(self.strTheme)

        txt = tkinter.Text(wind,height=300,width=300,bg=clr)
        txt.pack()

        txt.insert(tkinter.END, str_in)

    def show_all(self):
        tkinter.mainloop()

