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
        super().__init__(master = master, width = width, height = height, fg_color="#FFFAFA", corner_radius=30)

        self.pack_propagate(False)

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

    def lock_button_move(self) -> None:
        self.__move_btn.configure(state=tkinter.DISABLED)

    def unlock_button_move(self) -> None:
        self.__move_btn.configure(state=tkinter.NORMAL)

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

    BUILD = {
        1: (82, 62, 90, 78),
        2: (149, 62, 157, 78),
        4: (283, 62, 291, 78),
        6: (417, 62, 425, 78),
        7: (484, 62, 492, 78),
        9: (618, 62, 626, 78),
        11: (685, 82, 701, 90),
        12: (685, 149, 701, 157),
        14: (685, 283, 701, 291),
        16: (685, 417, 701, 425),
        17: (685, 484, 701, 492),
        19: (685, 618, 701, 626),
        21: (618, 685, 626, 703),
        22: (551, 685, 559, 703),
        24: (417, 685, 425, 703),
        26: (283, 685, 291, 703),
        27: (216, 685, 224, 703),
        29: (82, 685, 90, 703),
        31: (62, 618, 78, 626),
        32: (62, 551, 78, 559),
        34: (62, 417, 78, 425),
        36: (62, 283, 78, 291),
        37: (62, 216, 78, 224),
        39: (62, 82, 78, 90)
    }

    PLAYER_LABEL = {
        1: (110, 90),
        2: (177, 90),
        4: (311, 90),
        5: (378, 90),
        6: (445, 90),
        7: (512, 90),
        9: (646, 90),
        11: (673, 113),
        12: (673, 180),
        14: (673, 314),
        15: (673, 381),
        16: (673, 448),
        17: (673, 515),
        19: (673, 649),
        21: (646, 675),
        22: (579, 675),
        24: (445, 675),
        25: (378, 675),
        26: (311, 675),
        27: (244, 675),
        29: (110, 670),
        31: (90, 649),
        32: (90, 582),
        34: (90, 448),
        35: (90, 381),
        36: (90, 314),
        37: (90, 247),
        39: (90, 113)
    }


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

    def create_widgets(self, names: list[str], prices: list[int]) -> None:
        label1 = CTkLabel(self, text="Выберите собственность которую хотите продать", font=(FONT, 14, "bold"))
        label1.grid(row = 0, column = 0, padx = 30, pady=20, columnspan = 2)

        if not names:
            label2 = CTkLabel(self, text="У вас нет собственности для продажи")
            label2.grid(row = 1, column = 0, pady=20, columnspan = 2)

            return None

        self.__sell_index = tkinter.IntVar(value=0)

        for i in range(len(names)):
            rad_button = CTkRadioButton(master=self, value=i, text=names[i], variable=self.__sell_index, fg_color=SYSTEM_FG, hover_color = SYSTEM_HOVER, font=("Comic Sans MS", 14, "bold"))
            rad_button.grid(row = i + 1, column = 0, pady=10)

            price = CTkLabel(self, text=f"{prices[i]}$", font=(FONT, 14, "bold"))
            price.grid(row=i + 1, column=1, pady=10, padx=20)

        self.__sell_btn.grid(row = len(names) + 1, column = 0, pady=30, columnspan = 2)

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

    def create_widgets(self, names: list[str], prices: list[int]) -> None:
        label1 = CTkLabel(self, text="Выберите собственность которую хотите улучшить", font=(FONT, 14, "bold"))
        label1.grid(row=0, column = 0, padx = 30, pady=20, columnspan=2)

        if not names:
            label2 = CTkLabel(self, text="У вас нет собственности для улучшения")
            label2.grid(row=1, column=0, pady=20, columnspan= 2)

            return None

        self.__build_index = tkinter.IntVar(value=0)

        for i in range(len(names)):
            rad_button = CTkRadioButton(master=self, value=i, text=names[i], variable=self.__build_index, fg_color=SYSTEM_FG, hover_color = SYSTEM_HOVER, font=("Comic Sans MS", 14, "bold"))
            rad_button.grid(row= i + 1, column=0, pady=10)

            price = CTkLabel(self, text=f"{prices[i]}$", font=(FONT, 14, "bold"))
            price.grid(row=i + 1, column=1, pady=10, padx=20)

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



