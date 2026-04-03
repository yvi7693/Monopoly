from dataclasses import dataclass

from customtkinter import *
from PIL import Image

from src.view.widgets import Button


class InteractionWindow(CTkFrame):

    def __init__(self, master, width: int, height: int):
        super().__init__(master = master, width = width, height = height)

        self.grid_columnconfigure(0, weight=0, minsize=163)
        self.grid_columnconfigure(1, weight=0, minsize=163)
        self.grid_rowconfigure(0, weight=0)

        self.__dices = []

        self.__create_widgets()

    def update_widgets(self, id: int, balance: int, points_1: int, points_2: int) -> None:
        self.__player.configure(text = f"Player №{id+1}")
        self.__balance.configure(text = f"{balance} 💰")

        self.__dice_1.configure(image = self.__dices[points_1 - 1])
        self.__dice_2.configure(image=self.__dices[points_2 - 1])


    def add_listener_on_click_move(self, callback) -> None:
            self.__move_btn.add_listener(callback)

    def __create_widgets(self) -> None:
        self.__player = CTkLabel(master = self, text=f"Player №", fg_color="transparent", text_color="black", font=("Arial", 20), pady = 20)
        self.__player.grid(row=0, column=0, columnspan=2)

        self.__label_balance = CTkLabel(master=self, text="Balance:", fg_color="transparent", text_color="black")
        self.__label_balance.grid(row=1, column=0, padx=5, sticky="e")

        self.__balance = CTkLabel(master=self, text="💰", fg_color="transparent", text_color="black")
        self.__balance.grid(row=1, column=1, padx=0, sticky="w")

        self.__create_dice()

        self.__dice_1.grid(row = 2, column = 0, pady=(400,0), sticky = "e")
        self.__dice_2.grid(row=2, column=1, pady=(400, 0), sticky = "w")


        self.__move_btn = Button(self, "MOVE")
        self.__move_btn.grid(row = 3, column =0, pady=(100,0), columnspan=2)

    def __create_dice(self) -> None:

        self.__dices.append(CTkImage(light_image=Image.open("images/1.png"), dark_image=Image.open("images/1.png"),
                                  size=(70, 70)))
        self.__dices.append(CTkImage(light_image=Image.open("images/2.png"), dark_image=Image.open("images/2.png"),
                                   size=(70, 70)))
        self.__dices.append(CTkImage(light_image=Image.open("images/3.png"), dark_image=Image.open("images/3.png"),
                                   size=(70, 70)))
        self.__dices.append(CTkImage(light_image=Image.open("images/4.png"), dark_image=Image.open("images/4.png"),
                                   size=(70, 70)))
        self.__dices.append(CTkImage(light_image=Image.open("images/5.png"), dark_image=Image.open("images/5.png"),
                                   size=(70, 70)))
        self.__dices.append(CTkImage(light_image=Image.open("images/6.png"), dark_image=Image.open("images/6.png"),
                                   size=(70, 70)))

        self.__dice_1 = CTkLabel(self, text="")
        self.__dice_2 = CTkLabel(self, text="")


@dataclass
class CoordCells:

    TOP_X = list(range(50, 763, 67))
    RIGHT_Y = list(range(50, 763, 67))
    BOTTOM_X = list(range(720, 0, -67))
    LEFT_Y = list(range(720, 0, -67))
