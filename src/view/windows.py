from __future__ import annotations

import time
import tkinter
from tkinter import PhotoImage

from customtkinter import *

from src.constant_view import *
from src.view.widgets import Button, ProgressBar
from src.view.windows_lower import InteractionWindow, CoordCells
from tkinter.messagebox import showinfo, askyesno

from PIL import Image


class StartWindow(CTkFrame):

    __start_btn: Button | None
    __progressbar: ProgressBar | None
    __count_players: IntVar | None

    def __init__(self, master, width: int, height: int, bg_color):
        super().__init__(master = master, height = height, width = width, fg_color=bg_color)

        self.__progressbar = None
        self.__start_btn = None
        self.__count_players = None

        self.__create_widgets()

    def add_listener_on_click_start(self, callback) -> None:
        self.__start_btn.add_listener(callback)

    def start_loading(self) -> None:
        self.__progressbar = ProgressBar(self, PROGRESS_WIDTH, SYSTEM_FG)
        self.__progressbar.pack(pady=(100,0))
        self.__progressbar.start()

    def __create_widgets(self) -> None:
        logo = CTkImage(light_image=Image.open(PATH_LOGO_START),
                            dark_image=Image.open(PATH_LOGO_START),
                            size=(500, 100))

        logo_label = CTkLabel(self, image=logo, text="")
        logo_label.pack(pady=(100,0))

        radio_frame = CTkFrame(self, fg_color = RADIO_BG)
        radio_frame.pack(pady=(100,0))

        self.__count_players = tkinter.IntVar(value=2)

        players_2 = CTkRadioButton(radio_frame, text=RADIO_BUTTON_TEXT_2, variable=self.__count_players, value=2, fg_color=SYSTEM_FG, hover_color = SYSTEM_HOVER)
        players_3 = CTkRadioButton(radio_frame, text=RADIO_BUTTON_TEXT_3, variable=self.__count_players, value=3, fg_color=SYSTEM_FG, hover_color = SYSTEM_HOVER)
        players_4 = CTkRadioButton(radio_frame, text=RADIO_BUTTON_TEXT_4, variable=self.__count_players, value=4, fg_color=SYSTEM_FG, hover_color = SYSTEM_HOVER)
        players_5 = CTkRadioButton(radio_frame, text=RADIO_BUTTON_TEXT_5, variable=self.__count_players, value=5, fg_color=SYSTEM_FG, hover_color = SYSTEM_HOVER)
        players_6 = CTkRadioButton(radio_frame, text=RADIO_BUTTON_TEXT_6, variable=self.__count_players, value=6, fg_color=SYSTEM_FG, hover_color = SYSTEM_HOVER)

        players_2.pack(side = "left", pady = 20)
        players_3.pack(side = "left", pady = 20)
        players_4.pack(side = "left", pady = 20)
        players_5.pack(side = "left", pady = 20)
        players_6.pack(side = "left", pady = 20)

        self.__start_btn = Button(self, START_BUTTON_TEXT, )
        self.__start_btn.pack(pady = 100, anchor = "center", side="top")

    def __get_count_players(self) -> IntVar: return self.__count_players

    count_players = property(__get_count_players)


class PresentWindow(CTkFrame):

    __label_name: CTkLabel
    __label_present: CTkLabel

    __step: int
    __next_callback: None

    def __init__(self, master,  width: int, height: int, fg_color):
        super().__init__(master = master, width = width, height = height, fg_color = fg_color)

        self.__step = 0
        self.__callback = None

        self.__create_widgets()

    def start_animate(self, callback) -> None:
        self.__step = 0
        self.__display_text()

        self.__callback = callback

    def __create_widgets(self) -> None:

        self.__label_name = CTkLabel(self, text=NAME_PRESENT, text_color=START_COLOR, font=(FONT_PRESENT, FONT_SIZE_PRESENT))
        self.__label_name.place(relx=0.5, rely=0.5, anchor="center")

        self.__label_present = CTkLabel(self, text=TEXT_PRESENT, text_color=START_COLOR, font=(FONT_PRESENT, FONT_SIZE_PRESENT))
        self.__label_present.place(relx=0.5, rely=0.55, anchor="center")

    def __display_text(self) -> None:
        max_step = 150

        value = int((255 / max_step) * self.__step)

        color = f"#{value:02x}{value:02x}{value:02x}"

        self.__label_present.configure(text_color=color)
        self.__label_name.configure(text_color=color)

        self.__step += 1

        if self.__step < max_step:
            self.__step += 1
            self.after(50, self.__display_text)

        else:
            time.sleep(2)
            self.__callback()


class GameWindow(CTkFrame):

    __game_field: tkinter.Canvas | None
    __interaction_window: InteractionWindow | None

    __logo: PhotoImage

    def __init__(self, master, width: int, height: int):
        super().__init__(master=master, height=height, width=width)

        self.__game_field = None
        self.__interaction_window = None

        self.__tokens = []
        self.__tokens_image = []

        self.__logo = tkinter.PhotoImage(file = PATH_LOGO_GAME)

        self.__create_interaction_window()




    def add_listener_on_click_move(self, callback) -> None:
        self.__interaction_window.add_listener_on_click_move(callback)

    def update_widgets(self, id: int, balance: int, points_1: int, points_2: int, ownership: str) -> None:
        self.__interaction_window.update_widgets(id, balance, points_1, points_2, ownership)

    def create_game_field(self, names_cells: list[str], colors: list[str], count_players: int) -> None:
        self.__game_field = tkinter.Canvas(master=self, width=HEIGHT, height=HEIGHT, bg = FIELD_COLOR)
        self.__game_field.grid(row=0, column=0, sticky="w")

        self.__create_rectangles()
        self.__create_text(names_cells)
        self.__create_neighborhood(colors)
        self.__create_logo()
        self.__create_token_image()
        self.__create_token(count_players)

    def update_place_token(self, numer_token: int, position: int):

        if position <= 10:
            self.__game_field.coords(self.__tokens[numer_token], CoordCells.TOP_X[position], 50)

        elif position > 10 and position <= 20:
            self.__game_field.coords(self.__tokens[numer_token], 720, CoordCells.RIGHT_Y[position-10])

        elif position > 20 and position <= 30:
            self.__game_field.coords(self.__tokens[numer_token], CoordCells.BOTTOM_X[position - 20], 720)

        elif position > 30 and position <= 40:
            self.__game_field.coords(self.__tokens[numer_token], 50, CoordCells.RIGHT_Y[position - 30])

    def __create_interaction_window(self) -> None:
        self.__interaction_window = InteractionWindow(self, WIDTH_INTERACTIVE_WINDOW, HEIGHT)
        self.__interaction_window.grid(row=0, column=1, sticky="nswe")

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
        self.__game_field.create_image(380, 370, image = self.__logo)

    def __create_token(self, count_players: int) -> None:
        for i in range(count_players):
            self.__tokens.append(self.__game_field.create_image(50, 50,  image = self.__tokens_image[i]))

    def __create_token_image(self) -> None:
        self.__tokens_image.append(tkinter.PhotoImage(file = "images/token1.png"))
        self.__tokens_image.append(tkinter.PhotoImage(file="images/token2.png"))
        self.__tokens_image.append(tkinter.PhotoImage(file="images/token3.png"))
        self.__tokens_image.append(tkinter.PhotoImage(file="images/token4.png"))
        self.__tokens_image.append(tkinter.PhotoImage(file="images/token5.png"))
        self.__tokens_image.append(tkinter.PhotoImage(file="images/token6.png"))
