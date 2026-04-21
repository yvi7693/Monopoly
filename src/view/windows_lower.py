import tkinter
from dataclasses import dataclass

from customtkinter import *
from PIL import Image

from src.constant_view import *
from src.view.widgets import Button, ScrollableOwnerships


class InteractionWindow(CTkFrame):

    __label_player: CTkLabel
    __label_balance: CTkLabel
    __balance: CTkLabel
    __label_ownerships: CTkLabel
    __scroll_ownerships: ScrollableOwnerships

    def __init__(self, master, width: int, height: int):
        super().__init__(master = master, width = width, height = height, fg_color="#FFFAFA")

        self.grid_columnconfigure(0, weight=0, minsize=163)
        self.grid_columnconfigure(1, weight=0, minsize=163)
        self.grid_rowconfigure(0, weight=0)

        self.__dices = []

        self.__create_widgets()

    def update_widgets(self, id: int, balance: int, points_1: int, points_2: int, ownerships: str) -> None:
        self.__label_player.configure(text=f"{PLAYER_LABEL}{id + 1}")
        self.__balance.configure(text=f"{balance} 💰")

        self.__scroll_ownerships.update_text(text=f"{ownerships}")

        self.__dice_1.configure(image = self.__dices[points_1 - 1])
        self.__dice_2.configure(image=self.__dices[points_2 - 1])

    def add_listener_on_click_move(self, callback) -> None:
        self.__move_btn.add_listener(callback)

    def add_listener_on_click_sell(self, callback) -> None:
        self.__sell_btn.add_listener(callback)

    def add_listener_on_click_build(self, callback) -> None:
        self.__build_btn.add_listener(callback)

    def __create_widgets(self) -> None:
        frame = CTkFrame(master=self, height=200, corner_radius=100, fg_color="#e8e8e8")
        frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.__label_player = CTkLabel(master = frame, text=f"{PLAYER_LABEL}", fg_color="transparent", text_color=TEXT_COLOR, font=("San Francisco", FONT_SIZE_INTER, "bold"), pady = 20)
        self.__label_player.pack(anchor="center")

        self.__label_balance = CTkLabel(master=self, text=BALANCE_LABEL, fg_color="transparent", text_color=TEXT_COLOR, font=("San Francisco", 14, "bold"))
        self.__label_balance.grid(row=1, column=0, padx=5, sticky="e")

        self.__balance = CTkLabel(master=self, text=MONEY_EMOJI, fg_color="transparent", text_color=TEXT_COLOR, font=("San Francisco", 14, "bold"))
        self.__balance.grid(row=1, column=1, padx=0, sticky="w")

        self.__label_ownership = CTkLabel(master=self, text=OWNERSHIP_TEXT, fg_color="transparent", text_color=TEXT_COLOR,
                                 font=(FONT, FONT_SIZE_INTER))
        self.__label_ownership.grid(row=2, column=0, columnspan=2, pady=(30,0))

        self.__scroll_ownerships = ScrollableOwnerships(self,width=WIDTH_OWNERSHIP,height=HEIGHT_OWNERSHIP)
        self.__scroll_ownerships.grid(row=3, column=0, columnspan=2, sticky="nswe", pady=20)

        self.__sell_btn = Button(self, "SELL", width=80, fg_color="#696969", hover_color="#505050")
        self.__sell_btn.grid(row=4, column=0, padx=10, sticky="e")

        self.__build_btn = Button(self, "BUILD", width=80, fg_color="#696969", hover_color="#505050")
        self.__build_btn.grid(row=4, column=1, padx=10, sticky="w")

        self.__create_dice()

        self.__dice_1.grid(row = 5, column = 0, pady=(50,0), sticky = "e")
        self.__dice_2.grid(row=5, column=1, pady=(100, 0), sticky = "w")

        self.__move_btn = Button(self, MOVE_BUTTON_TEXT)
        self.__move_btn.grid(row = 6, column =0, pady=(50,0), columnspan=2)

    def __create_dice(self) -> None:

        self.__dices.append(CTkImage(light_image=Image.open(PATH_DICE1), dark_image=Image.open(PATH_DICE1),
                                  size=(SIZE_DICE, SIZE_DICE)))

        self.__dices.append(CTkImage(light_image=Image.open(PATH_DICE2), dark_image=Image.open(PATH_DICE2),
                                   size=(SIZE_DICE, SIZE_DICE)))

        self.__dices.append(CTkImage(light_image=Image.open(PATH_DICE3), dark_image=Image.open(PATH_DICE3),
                                   size=(SIZE_DICE, SIZE_DICE)))

        self.__dices.append(CTkImage(light_image=Image.open(PATH_DICE4), dark_image=Image.open(PATH_DICE4),
                                   size=(SIZE_DICE, SIZE_DICE)))

        self.__dices.append(CTkImage(light_image=Image.open(PATH_DICE5), dark_image=Image.open(PATH_DICE5),
                                   size=(SIZE_DICE, SIZE_DICE)))

        self.__dices.append(CTkImage(light_image=Image.open(PATH_DICE6), dark_image=Image.open(PATH_DICE6),
                                   size=(SIZE_DICE, SIZE_DICE)))

        self.__dice_1 = CTkLabel(self, text="", width=SIZE_DICE, height=SIZE_DICE)
        self.__dice_2 = CTkLabel(self, text="", width=SIZE_DICE, height=SIZE_DICE)


@dataclass
class CoordCells:

    TOP_X = list(range(50, 763, 67))
    RIGHT_Y = list(range(50, 763, 67))
    BOTTOM_X = list(range(720, 0, -67))
    LEFT_Y = list(range(720, 0, -67))

    FIRST_FIELD = TOP_X + RIGHT_Y
    TWICE_FIELD = BOTTOM_X + LEFT_Y



class SellWindow(CTkToplevel):

    def __init__(self, master):
        super().__init__(master = master)
        self.title("Sell Ownership")

        self.transient(master)
        self.lift()
        self.focus_force()
        self.grab_set()

        self.protocol("WM_DELETE_WINDOW", self.close)

        self.__sell_btn = Button(master = self, text = "SELL", width=110)
        self.__sell_index = None

    def get_sell_index(self) -> int:
        return self.__sell_index.get()

    def create_widgets(self, names: list[str]) -> None:
        label1 = CTkLabel(self, text="Выберите собственность которую хотите продать", font=(FONT, 14, "bold"))
        label1.pack(padx = 30, pady=20)

        if not names:
            label2 = CTkLabel(self, text="У вас нет собственности для продажи")
            label2.pack(pady=20)

            return None

        self.__sell_index = tkinter.IntVar(value=0)

        for i in range(len(names)):
            rad_button = CTkRadioButton(master=self, value=i, text=names[i], variable=self.__sell_index, fg_color=SYSTEM_FG, hover_color = SYSTEM_HOVER, font=("Comic Sans MS", 14, "bold"))
            rad_button.pack(pady=10)

        self.__sell_btn.pack(pady=30)

        return None

    def close(self) -> None:
        self.grab_release()
        self.destroy()

    def add_listener_on_click_sell(self, callback) -> None:
        self.__sell_btn.add_listener(callback)


class BuildWindow(CTkToplevel):

    def __init__(self, master):
        super().__init__(master = master)
        self.title("Building")

        self.transient(master)
        self.lift()
        self.focus_force()
        self.grab_set()

        self.protocol("WM_DELETE_WINDOW", self.close)

        self.__home_button = Button(master=self, text="HOME", fg_color="#3CB371", hover_color="#006400", width = 110)
        self.__hotel_button = Button(master=self, text="HOTEL", width = 110)

        self.__build_index = None

    def get_build_index(self) -> int:
        return self.__build_index.get()

    def create_widgets(self, names: list[str]) -> None:
        label1 = CTkLabel(self, text="Выберите собственность которую хотите улучшить", font=(FONT, 14, "bold"))
        label1.grid(row=0, column = 0, padx = 30, pady=20, columnspan=2)

        if not names:
            label2 = CTkLabel(self, text="У вас нет собственности для улучшения")
            label2.grid(row=1, column=0, pady=20, columnspan= 2)

            return None

        self.__build_index = tkinter.IntVar(value=0)

        for i in range(len(names)):
            rad_button = CTkRadioButton(master=self, value=i, text=names[i], variable=self.__build_index, fg_color=SYSTEM_FG, hover_color = SYSTEM_HOVER, font=("Comic Sans MS", 14, "bold"))
            rad_button.grid(row= i + 1, column=0, pady=10, columnspan=2)

        self.__home_button.grid(row=len(names)+1, column=0, pady=10, sticky="e", padx=10)
        self.__hotel_button.grid(row=len(names)+1, column=1, pady=10, sticky="w", padx=10)

        return None

    def close(self) -> None:
        self.grab_release()
        self.destroy()

    def add_listener_on_click_home(self, callback) -> None:
        self.__home_button.add_listener(callback)

    def add_listener_on_click_hotel(self, callback) -> None:
        self.__hotel_button.add_listener(callback)



