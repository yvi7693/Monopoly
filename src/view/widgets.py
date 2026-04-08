import time

from customtkinter import CTkButton, CTkProgressBar, CTkScrollableFrame, CTkLabel

from src.constant_view import EMPTY_TEXT, SYSTEM_FG, SYSTEM_HOVER


class Button(CTkButton):

    def __init__(self, master, text, callback=None, fg_color=SYSTEM_FG, hover_color = SYSTEM_HOVER):
        super().__init__(master=master, text=text, command = self.__handler_click, fg_color = fg_color, hover_color = hover_color)

        self.__callback = callback

    def add_listener(self, callback) -> None:
        self.__callback = callback

    def __handler_click(self) -> None:
        self.__callback()


class ProgressBar(CTkProgressBar):

    __progress: int

    def __init__(self, master, width, progress_color):
        super().__init__(master = master, width = width, progress_color = progress_color)

        self.__progress = 0

    def start(self) -> None:
        speed = 0.1

        while self.__progress < 1:
            time.sleep(0.1)
            self.__progress += speed

            self.set(self.__progress)

            self.update()

class ScrollableOwnerships(CTkScrollableFrame):
    
    def __init__(self, master, width: int, height: int):
        super().__init__(master=master, width=width, height=height)

        self.__label = CTkLabel(self, text = EMPTY_TEXT)
        self.__label.grid(row=0, column=0, padx=20)

    def update_text(self, text: str):
        self.__label.configure(text=text)