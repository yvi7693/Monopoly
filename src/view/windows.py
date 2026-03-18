from customtkinter import *

class MainWindow(CTk):


    def __init__(self, width: int, height: int):
        super().__init__()

        self.geometry(f"{width}x{height}")
        self.resizable(False, False)

        self.__callback_on_start = None

        self.__create_widgets()

    def loop(self):
        self.mainloop()


    def add_listener_on_click_start(self, callback):
        self.__callback_on_start = callback

    def __handler_on_click_start(self):
        self.__callback_on_start()

    def __create_widgets(self):
        start_btn = CTkButton(master=self, text="Start Game", command=self.__handler_on_click_start)
        start_btn.pack(anchor=CENTER)

# MainWindow(600, 500).loop()