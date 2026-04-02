import time

from customtkinter import CTkButton, CTkProgressBar


class MyButton(CTkButton):

    def __init__(self, master, text, callback=None, bg_color="#DC143C", fg_color="#DC143C", hover_color = "#DC143C"):
        super().__init__(master=master, text=text, command = self.__handler_click, bg_color = bg_color, fg_color = fg_color, hover_color = hover_color)

        self.__callback = callback

    def add_listener(self, callback) -> None:
        self.__callback = callback

    def __handler_click(self) -> None:
        self.__callback()


class ProgressBar(CTkProgressBar):

    __progress: int

    def __init__(self, master, orientation, mode, width, progress_color, corner_radius):
        super().__init__(master = master, orientation = orientation, mode = mode, width = width, progress_color = progress_color, corner_radius = corner_radius)

        self.__progress = 0



    def start(self) -> None:
        speed = 0.1

        while self.__progress < 1:
            time.sleep(0.1)
            self.__progress += speed

            self.set(self.__progress)

            self.update()