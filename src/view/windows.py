from __future__ import annotations

import math
import time
import tkinter
from tkinter import PhotoImage
from pygame import mixer

from customtkinter import *

from src.view.constant_view import *
from src.view.widgets import Button, ProgressBar
from src.view.windows_lower import InteractionWindow, CoordCells

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

    def lock_button(self) -> None:
        self.__start_btn.configure(state=tkinter.DISABLED)

    def unlock_button(self) -> None:
        self.__start_btn.configure(state=tkinter.NORMAL)

    def add_listener_on_click_start(self, callback) -> None:
        self.__start_btn.add_listener(callback)

    def start_loading(self) -> None:
        mixer.music.fadeout(3000)

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

        players_2 = CTkRadioButton(radio_frame, text=RADIO_BUTTON_TEXT_2, variable=self.__count_players, value=2, fg_color=SYSTEM_FG, hover_color = SYSTEM_HOVER, font=("Comic Sans MS", 14, "bold"))
        players_3 = CTkRadioButton(radio_frame, text=RADIO_BUTTON_TEXT_3, variable=self.__count_players, value=3, fg_color=SYSTEM_FG, hover_color = SYSTEM_HOVER, font=("Comic Sans MS", 14, "bold"))
        players_4 = CTkRadioButton(radio_frame, text=RADIO_BUTTON_TEXT_4, variable=self.__count_players, value=4, fg_color=SYSTEM_FG, hover_color = SYSTEM_HOVER, font=("Comic Sans MS", 14, "bold"))
        players_5 = CTkRadioButton(radio_frame, text=RADIO_BUTTON_TEXT_5, variable=self.__count_players, value=5, fg_color=SYSTEM_FG, hover_color = SYSTEM_HOVER, font=("Comic Sans MS", 14, "bold"))
        players_6 = CTkRadioButton(radio_frame, text=RADIO_BUTTON_TEXT_6, variable=self.__count_players, value=6, fg_color=SYSTEM_FG, hover_color = SYSTEM_HOVER, font=("Comic Sans MS", 14, "bold"))

        players_2.pack(side = "left", pady = 20)
        players_3.pack(side = "left", pady = 20)
        players_4.pack(side = "left", pady = 20)
        players_5.pack(side = "left", pady = 20)
        players_6.pack(side = "left", pady = 20)

        self.__start_btn = Button(self, START_BUTTON_TEXT)
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
        max_step = 70

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
        self.__tokens_active_image = []
        self.__tokens_position = []

        self.__builds = {}
        self.__label_own = {}

        self.__current_token = None

        self.__callback_past_animate = None

        self.__logo = tkinter.PhotoImage(file = PATH_LOGO_GAME)

        self.__create_interaction_window()

        self.__start_position_field = 150
        self.__stop_position_field = 0

        self.__stop_position_frame = 770

        self.__go_btn = None

    def create_owner_label(self, player_id: int, position: int) -> None:
        x,y = CoordCells.PLAYER_LABEL[position]

        label = self.__game_field.create_text(x, y, text=f"P{player_id}", font=(FONT, 14, "bold"))
        self.__label_own[position] = label

    def delete_owner_label(self, position: int) -> None:
        self.__game_field.delete(self.__label_own[position])

    def create_home(self, position: int, index_home: int) -> None:
        if position not in self.__builds:
            self.__builds[position] = []

        x1, y1, x2, y2 = CoordCells.BUILD[position]

        if position < 10 or position > 20 and position < 30:
            house = self.__game_field.create_rectangle(x1 + (10 * index_home), y1, x2 + (10 * index_home), y2, fill="green")

        else:
            house = self.__game_field.create_rectangle(x1, y1 + (10 * index_home), x2, y2 + (10 * index_home), fill="green")

        self.__builds[position].append(house)

    def delete_builds(self, position: int) -> None:
        if not position in self.__builds: return None

        for build in self.__builds[position]:
            self.__game_field.delete(build)

        return None

    def create_hotel(self, position: int) -> None:
        self.delete_builds(position)

        x1, y1, x2, y2 = CoordCells.BUILD[position]

        if position < 10 or position > 20 and position < 30:
            hotel = self.__game_field.create_rectangle(x1, y1, x2, y2,
                                                       fill="red")

        else:
            hotel = self.__game_field.create_rectangle(x1, y1, x2, y2,
                                                       fill="red")

        self.__builds[position].append(hotel)

    def create_game_field(self, names_cells: list[str], colors: list[str], count_players: int) -> None:
        self.__game_field = tkinter.Canvas(master=self, width=HEIGHT, height=HEIGHT, bg = FIELD_COLOR)
        self.__game_field.place(x=self.__start_position_field)

        self.__create_rectangles()
        self.__create_text(names_cells)
        self.__create_neighborhood(colors)
        self.__create_logo()
        self.__create_token_image()
        self.__create_token(count_players)

    def create_go_btn(self) -> None:
        self.__go_btn = Button(master=self, text="GO!", width = 50, height= 40)
        self.__go_btn.add_listener(self.animate_slide_field)
        self.__go_btn.place(x=500, y=500)

    def animate_slide_field(self) -> None:
        self.__go_btn.destroy()

        if self.__start_position_field > self.__stop_position_field:
            self.__start_position_field -= 5
            self.__game_field.place(x=self.__start_position_field)

            self.after(5, self.animate_slide_field)

        else:
            self.animate_slide_frame()

    def animate_slide_frame(self) -> None:
        if self.__start_position_frame > self.__stop_position_frame:
            self.__start_position_frame -= 5
            self.__interaction_window.place(x=self.__start_position_frame)

            self.after(5, self.animate_slide_frame)

    def get_interaction_window(self) -> InteractionWindow:
        return self.__interaction_window

    def set_callback_past_animate(self, callback) -> None:
        self.__callback_past_animate = callback

    def add_listener_on_click_move(self, callback) -> None:
        self.__interaction_window.add_listener_on_click_move(callback)

    def add_listener_on_click_sell(self, callback) -> None:
        self.__interaction_window.add_listener_on_click_sell(callback)

    def add_listener_on_click_build(self, callback) -> None:
        self.__interaction_window.add_listener_on_click_build(callback)

    def update_widgets(self, id: int, balance: int, points_1: int, points_2: int, ownership: str) -> None:
        self.__interaction_window.update_widgets(id, balance, points_1, points_2, ownership)

    def animate_move_token(self, number_token: int, position: int, callback) -> None:

        current_position = self.__tokens_position[number_token]

        if current_position < 10:
            self.__game_field.move(self.__tokens[number_token], 67, 0)

        elif current_position >= 10 and current_position < 20:
            self.__game_field.move(self.__tokens[number_token], 0, 67)

        elif current_position >= 20 and current_position < 30:
            self.__game_field.move(self.__tokens[number_token], -67, 0)

        elif current_position >= 30 and current_position < 40:
            self.__game_field.move(self.__tokens[number_token], 0, -67)

        self.__tokens_position[number_token] += 1

        if self.__tokens_position[number_token] == 40:
            self.__tokens_position[number_token] = 0

        if not self.__tokens_position[number_token] == position:
            self.__game_field.after(80, self.animate_move_token, number_token, position, callback)

        else:
            self.__game_field.update_idletasks()
            callback(position)

        return None

    def update_place_token(self, number_token: int, position: int) -> None:
        self.__activate_token(number_token)

        self.animate_move_token(number_token, position, self.past_animation)

    def past_animation(self, position: int):
        self.find_overlay_tokens(position)
        self.__callback_past_animate()

    def find_overlay_tokens(self, position: int) -> None:
        overlay_index = []

        for i in range(len(self.__tokens_position)):
            if self.__tokens_position[i] == position:
                overlay_index.append(i)

        if len(overlay_index) >= 2:
            self.__offset_token(overlay_index, position)

        if len(overlay_index) == 1:
            x, y = self.__cell_center(position)
            self.__game_field.coords(self.__tokens[overlay_index[0]], x, y)

    def delete_token(self, id: int) -> None:
        self.__game_field.itemconfig(self.__tokens[id], state='hidden')
        self.__tokens_position[id] = None

    def __create_interaction_window(self) -> None:
        self.__start_position_frame = 1100

        self.__interaction_window = InteractionWindow(self, WIDTH_INTERACTIVE_WINDOW, HEIGHT)
        self.__interaction_window.place(x=self.__start_position_frame)

    def __activate_token(self, number_token: int) -> None:
        if self.__current_token is not None:
            self.__game_field.itemconfig(self.__tokens[self.__current_token], image=self.__tokens_image[self.__current_token])

        self.__game_field.itemconfig(self.__tokens[number_token], image=self.__tokens_active_image[number_token])
        self.__current_token = number_token

    def __create_rectangles(self) -> None:

        for i in range(80, 683, 67):
            self.__game_field.create_rectangle(i, 0, i+67, 80, outline="#FFFFFF", width=3)
            self.__game_field.create_rectangle(i, 683, i + 67, 763, outline="#FFFFFF", width=3)
            self.__game_field.create_rectangle(683, i, 763, i + 67, outline="#FFFFFF", width=3)
            self.__game_field.create_rectangle(0, i, 80, i + 67, outline="#FFFFFF", width=3)

        self.__game_field.create_rectangle(0, 0, 80, 80, outline="#FFFFFF", width=3)
        self.__game_field.create_rectangle(683, 0, 763, 80, outline="#FFFFFF", width=3)
        self.__game_field.create_rectangle(0, 683, 80, 763, outline="#FFFFFF", width=3)
        self.__game_field.create_rectangle(683, 683, 763, 763, outline="#FFFFFF", width=3)

    def __create_text(self, names_cells: list[str]) -> None:

        index = 0

        for i in range(45, 763, 67):
            self.__game_field.create_text(i, 40 , text = names_cells[index], font=("Comic Sans MS", 13))
            index += 1

        for i in range(115, 700, 67):
            self.__game_field.create_text(730, i, text = names_cells[index], font=("Comic Sans MS", 13))
            index += 1

        for i in range(715, 20, -67):
            self.__game_field.create_text(i, 725, text = names_cells[index], font=("Comic Sans MS", 13))
            index += 1

        for i in range(650, 80, -67):
            self.__game_field.create_text(30, i, text = names_cells[index], font=("Comic Sans MS", 13))
            index += 1

    def __create_neighborhood(self, colors: list[str]) -> None:

        index = 0

        coord_first = [80, 147, 281, 415, 482, 616]
        coord_last = [683, 616, 482, 348, 281, 147]


        for x in coord_first:
            self.__game_field.create_rectangle(x, 60, x + 67, 80, fill = colors[index], outline="#FFFFFF")
            index += 1

        for y in coord_first:
            self.__game_field.create_rectangle(683, y, 705, y + 67, fill = colors[index], outline="#FFFFFF")
            index += 1

        for x in coord_last:
            self.__game_field.create_rectangle(x, 683, x-67, 705, fill = colors[index], outline="#FFFFFF")
            index += 1

        for y in coord_last:
            self.__game_field.create_rectangle(60, y, 80, y-67, fill = colors[index], outline="#FFFFFF")
            index += 1

    def __create_logo(self) -> None:
        self.__game_field.create_image(380, 370, image = self.__logo)

    def __create_token(self, count_players: int) -> None:
        for i in range(count_players):
            self.__tokens.append(self.__game_field.create_image(50, 50,  image = self.__tokens_image[i]))
            self.__tokens_position.append(0)

    def __create_token_image(self) -> None:
        self.__tokens_image.append(tkinter.PhotoImage(file = "images/token1.png"))
        self.__tokens_image.append(tkinter.PhotoImage(file="images/token2.png"))
        self.__tokens_image.append(tkinter.PhotoImage(file="images/token3.png"))
        self.__tokens_image.append(tkinter.PhotoImage(file="images/token4.png"))
        self.__tokens_image.append(tkinter.PhotoImage(file="images/token5.png"))
        self.__tokens_image.append(tkinter.PhotoImage(file="images/token6.png"))

        self.__tokens_active_image.append(tkinter.PhotoImage(file="images/active_token1.png"))
        self.__tokens_active_image.append(tkinter.PhotoImage(file="images/active_token2.png"))
        self.__tokens_active_image.append(tkinter.PhotoImage(file="images/active_token3.png"))
        self.__tokens_active_image.append(tkinter.PhotoImage(file="images/active_token4.png"))
        self.__tokens_active_image.append(tkinter.PhotoImage(file="images/active_token5.png"))
        self.__tokens_active_image.append(tkinter.PhotoImage(file="images/active_token6.png"))

    def __offset_token(self, overlay_index: list[int], position: int) -> None:

        base_x, base_y = self.__cell_center(position)

        count = len(overlay_index)

        radius = min(30, 10 + count * 4)

        for i, token_idx in enumerate(overlay_index):
            angle = (2 * math.pi * i) / count
            dx = radius * math.cos(angle)
            dy = radius * math.sin(angle)
            self.__game_field.coords(self.__tokens[token_idx], base_x + dx, base_y + dy)

        return None

    @staticmethod
    def __cell_center(position: int) -> tuple[int, int] | None:
        if position <= 10:
            return CoordCells.TOP_X[position], 50
        if position <= 20:
            return 720, CoordCells.RIGHT_Y[position - 10]
        if position <= 30:
            return CoordCells.BOTTOM_X[position - 20], 720
        if position <= 40:
            return 50, CoordCells.LEFT_Y[position - 30]

        return None


class WinnerWindow(CTkFrame):

    def __init__(self, master, width: int, height: int):
        super().__init__(master=master, width=width, height=height)

        self.__restart_btn = Button(self, "Restart")

    def create_widgets(self, id: int) -> None:

        my_image = CTkImage(light_image=Image.open("images/MrMonopoly.png"),
                                          dark_image=Image.open("images/MrMonopoly.png"),
                                          size=(400, 400))

        image_label = CTkLabel(self, image=my_image, text="")
        image_label.pack()

        label_win = CTkLabel(self, text="WINNER", fg_color="transparent", text_color="red", font=(FONT_PRESENT, 60, "bold"))
        label_win.pack(anchor="center", pady=(20, 0))

        label_win = CTkLabel(self, text=f"Player №{id + 1}", fg_color="transparent", font=(FONT_PRESENT, 30))
        label_win.pack(anchor="center", pady=10)

        self.__restart_btn.pack(pady = (60, 0))

    def add_listener_on_click_restart(self, callback) -> None:
        self.__restart_btn.add_listener(callback)

    def lock_button_restart(self) -> None:
        self.__restart_btn.configure(state=tkinter.DISABLED)

    def unlock_button_restart(self) -> None:
        self.__restart_btn.configure(state=tkinter.NORMAL)



