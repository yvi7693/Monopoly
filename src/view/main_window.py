from customtkinter import CTk

from src.view.windows import StartWindow, PresentWindow, GameWindow


class MainWindow(CTk):

    __start_window: StartWindow
    __present_window: PresentWindow
    __game_window: GameWindow

    def __init__(self, width: int, height: int):
        super().__init__()

        self.geometry(f"{width}x{height}")
        self.resizable(False, False)

        self.__start_window = StartWindow(self, 1100, 763)


        self.__start_window.pack()


    def loop(self):
        self.mainloop()

    def show_present_window(self):
        self.__present_window.tkraise()
        self.__present_window.start_animate(self.show_game_window)

    def show_game_window(self) -> None:
        self.__game_window.tkraise()

    def create_game_field(self, names_cells: list[str]):
        self.__game_window.create_field(names_cells)


    def __get_start_window(self) -> StartWindow: return self.__start_window

    start_window = property(__get_start_window)