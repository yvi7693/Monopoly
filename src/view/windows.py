from __future__ import annotations

import tkinter
from customtkinter import *
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

        self.__game_field = None

        self.__logo = tkinter.PhotoImage(file="logo.png")

    def create_field(self, names_cells: list[str], colors: list[str]) -> None:
        self.__game_field = CTkCanvas(master=self, width=763, height=763, bg = "#c7f4bd")
        self.__game_field.pack(anchor="w")

        self.__create_rectangles()
        self.__create_text(names_cells)
        self.__create_neighborhood(colors)
        self.__create_logo()

    def __create_rectangles(self) -> None:

        for i in range(80, 683, 67):
            self.__game_field.create_rectangle(i, 0, i+67, 80)
            self.__game_field.create_rectangle(i, 683, i + 67, 763)
            self.__game_field.create_rectangle(683, i, 763, i + 67)
            self.__game_field.create_rectangle(0, i, 80, i + 67)

        self.__game_field.create_rectangle(0, 0, 80, 80)
        self.__game_field.create_rectangle(683, 0, 763, 80)
        self.__game_field.create_rectangle(0, 683, 80, 763)
        self.__game_field.create_rectangle(683, 683, 763, 763)

    def __create_text(self, names_cells: list[str]) -> None:

        index = 0

        for i in range(45, 763, 67):
            self.__game_field.create_text(i, 40 , text = names_cells[index])
            index += 1

        for i in range(115, 700, 67):
            self.__game_field.create_text(730, i, text = names_cells[index])
            index += 1

        for i in range(715, 20, -67):
            self.__game_field.create_text(i, 725, text = names_cells[index])
            index += 1

        for i in range(650, 80, -67):
            self.__game_field.create_text(30, i, text = names_cells[index])
            index += 1

    def __create_neighborhood(self, colors: list[str]) -> None:

        index = 0

        coord_first = [80, 147, 281, 415, 482, 616]
        coord_last = [683, 616, 482, 348, 281, 147]


        for x in coord_first:
            self.__game_field.create_rectangle(x, 60, x + 67, 80, fill = colors[index])
            index += 1

        for y in coord_first:
            self.__game_field.create_rectangle(683, y, 705, y + 67, fill = colors[index])
            index += 1

        for x in coord_last:
            self.__game_field.create_rectangle(x, 683, x-67, 705, fill = colors[index])
            index += 1

        for y in coord_last:
            self.__game_field.create_rectangle(60, y, 80, y-67, fill = colors[index])
            index += 1

    def __create_logo(self) -> None:
        self.__game_field.create_image(380, 370, image=self.__logo)








