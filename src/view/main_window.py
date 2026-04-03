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

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.__start_window = StartWindow(self, 1100, 763, "#D8BFD8")
        self.__present_window = PresentWindow(self, 1100, 763, "black")
        self.__game_window = GameWindow(self, 1100, 763)

        self.__start_window.grid(row=0, column=0, sticky="nsew")
        self.__present_window.grid(row=0, column=0, sticky="nsew")
        self.__game_window.grid(row=0, column=0, sticky="nsew")

        self.__start_window.tkraise()


    def loop(self):
        self.mainloop()

    def show_present_window(self):
        self.__present_window.tkraise()
        self.__present_window.start_animate(self.show_game_window)

    def show_game_window(self) -> None:
        self.__game_window.tkraise()

    def update_window(self, id: int, balance: int, position: int) -> None:
        self.__game_window.update_widgets(id, balance)
        self.__game_window.update_place_token(id, position)

    def create_game_field(self, names_cells: list[str], colors: list[str], count_players: int):
        self.__game_window.create_game_field(names_cells, colors, count_players)

    def __get_start_window(self) -> StartWindow: return self.__start_window

    def __get_game_window(self) -> GameWindow: return self.__game_window

    start_window = property(__get_start_window)
    game_window = property(__get_game_window)

