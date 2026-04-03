from src.controllers.core import Game
from src.view.main_window import MainWindow

class GamePresenter:

    def __init__(self):
        self.__game = Game()

        self.__game_view = MainWindow(1100, 763)

        self.__game_view.start_window.add_listener_on_click_start(self.run)
        self.__game_view.game_window.add_listener_on_click_move(self.make_move)

        self.__game_view.loop()

    def run(self) -> None:

        self.__game.set_up(self.__game_view.start_window.radio_var.get())

        self.__game_view.create_game_field(self.__game.board.get_name_cells(), self.__game.board.get_colors(), self.__game_view.start_window.radio_var.get())

        self.__game_view.start_window.start_loading()
        self.__game_view.show_game_window()

    def make_move(self) -> None:
        self.__game.make_move()

        id = self.__game.get_current_player().id.get_value()
        balance = self.__game.get_current_balance()
        position = self.__game.get_current_player().get_position()

        self.__game_view.update_window(id , balance, position)





