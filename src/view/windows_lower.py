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
        super().__init__(master = master, width = width, height = height)

        self.grid_columnconfigure(0, weight=0, minsize=163)
        self.grid_columnconfigure(1, weight=0, minsize=163)
        self.grid_rowconfigure(0, weight=0)

        self.__dices = []

        self.__create_widgets()

    def update_widgets(self, id: int, balance: int, points_1: int, points_2: int, ownerships: str) -> None:
        self.__label_player.configure(text = f"{PLAYER_LABEL}{id+1}")
        self.__balance.configure(text = f"{balance} 💰")

        self.__scroll_ownerships.update_text(text=f"{ownerships}")

        self.__dice_1.configure(image = self.__dices[points_1 - 1])
        self.__dice_2.configure(image=self.__dices[points_2 - 1])

    def add_listener_on_click_move(self, callback) -> None:
            self.__move_btn.add_listener(callback)

    def __create_widgets(self) -> None:
        self.__label_player = CTkLabel(master = self, text=f"{PLAYER_LABEL}", fg_color="transparent", text_color=TEXT_COLOR, font=(FONT, FONT_SIZE_INTER), pady = 20)
        self.__label_player.grid(row=0, column=0, columnspan=2)

        self.__label_balance = CTkLabel(master=self, text=BALANCE_LABEL, fg_color="transparent", text_color=TEXT_COLOR)
        self.__label_balance.grid(row=1, column=0, padx=5, sticky="e")

        self.__balance = CTkLabel(master=self, text=MONEY_EMOJI, fg_color="transparent", text_color=TEXT_COLOR)
        self.__balance.grid(row=1, column=1, padx=0, sticky="w")

        self.__label_ownership = CTkLabel(master=self, text=OWNERSHIP_TEXT, fg_color="transparent", text_color=TEXT_COLOR,
                                 font=(FONT, FONT_SIZE_INTER), pady=0)
        self.__label_ownership.grid(row=2, column=0, columnspan=2)

        self.__scroll_ownerships = ScrollableOwnerships(self,width=WIDTH_OWNERSHIP,height=HEIGHT_OWNERSHIP)
        self.__scroll_ownerships.grid(row=3, column=0, columnspan=2, sticky="nswe", pady=20)

        self.__create_dice()

        self.__dice_1.grid(row = 4, column = 0, pady=(100,0), sticky = "e")
        self.__dice_2.grid(row=4, column=1, pady=(150, 0), sticky = "w")

        self.__move_btn = Button(self, MOVE_BUTTON_TEXT)
        self.__move_btn.grid(row = 5, column =0, pady=(100,0), columnspan=2)

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
