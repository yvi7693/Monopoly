from __future__ import annotations

import tkinter

from customtkinter import *
from PIL import Image

from src.view.widgets import Button, ProgressBar


class StartWindow(CTkFrame):

    __start_btn: Button | None
    __progressbar: ProgressBar | None

    def __init__(self, master, width: int, height: int):
        super().__init__(master = master, height = height, width = width)

        self.__progressbar = None
        self.__start_btn = None

        self.__create_widgets()

    def add_listener_on_click_start(self, callback) -> None:
        self.__start_btn.add_listener(callback)

    def start_loading(self) -> None:
        self.__progressbar = ProgressBar(self, 800, "red")
        self.__progressbar.pack(pady=(200,0))
        self.__progressbar.start()

    def __create_widgets(self) -> None:
        radio_frame = CTkFrame(self)
        radio_frame.pack(pady=(200,0))

        radio_var = tkinter.IntVar(value=0)

        players_2 = CTkRadioButton(radio_frame, text="2 Players", command=None, variable=radio_var, value=1)
        players_3 = CTkRadioButton(radio_frame, text="3 Players", command=None, variable=radio_var, value=2)
        players_4 = CTkRadioButton(radio_frame, text="4 Players", command=None, variable=radio_var, value=3)
        players_5 = CTkRadioButton(radio_frame, text="5 Players", command=None, variable=radio_var, value=4)
        players_6 = CTkRadioButton(radio_frame, text="6 Players", command=None, variable=radio_var, value=5)

        players_2.pack(side="left", pady = 20)
        players_3.pack(side="left", pady = 20)
        players_4.pack(side="left", pady = 20)
        players_5.pack(side="left", pady = 20)
        players_6.pack(side="left", pady = 20)

        self.__start_btn = Button(self, "Start", )
        self.__start_btn.pack(pady = 100, anchor = "center", side="top")




class PresentWindow(CTkFrame):

    def __init__(self, master, width: int, height: int):
        super().__init__(master=master, height=height, width=width)


class GameWindow(CTkFrame):

    def __init__(self, master, width: int, height: int):
        super().__init__(master=master, height=height, width=width)