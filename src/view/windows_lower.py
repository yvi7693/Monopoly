from customtkinter import *

from src.view.widgets import Button


class InteractionWindow(CTkFrame):

    def __init__(self, master, width: int, height: int):
        super().__init__(master = master, width = width, height = height)

        self.grid_columnconfigure(0, weight=0, minsize=163)
        self.grid_columnconfigure(1, weight=0, minsize=163)
        self.grid_rowconfigure(0, weight=0)

        self.__create_widgets()

    def update_widgets(self, id: int, balance: int) -> None:
        self.__player.configure(text = f"Player №{id}")
        self.__balance.configure(text = f"{balance} 💰")

    def __create_widgets(self) -> None:
        self.__player = CTkLabel(master = self, text=f"Player №", fg_color="transparent", text_color="black", font=("Arial", 20), pady = 20)
        self.__player.grid(row=0, column=0, columnspan=2)

        self.__label_balance = CTkLabel(master=self, text="Balance:", fg_color="transparent", text_color="black")
        self.__label_balance.grid(row=1, column=0, padx=5, sticky="e")

        self.__balance = CTkLabel(master=self, text="💰", fg_color="transparent", text_color="black")
        self.__balance.grid(row=1, column=1, padx=0, sticky="w")

        self.__move_btn = Button(self, "MOVE")
        self.__move_btn.grid(row = 2, column =0, pady=(620,0), columnspan=2)

    def add_listener_on_click_move(self, callback) -> None:
        self.__move_btn.add_listener(callback)
