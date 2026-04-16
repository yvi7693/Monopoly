from src.constant_view import WIDTH, HEIGHT
from src.controllers.core import Game

from src.view.main_window import MainWindow
from src.view.message import MessageDropper


class GamePresenter:

    __game: Game
    __game_view: MainWindow

    def __init__(self):
        self.__game = Game()
        self.__game_view = MainWindow(WIDTH, HEIGHT)

        self.__game_view.start_window.add_listener_on_click_start(self.run)

        self.__game_view.game_window.add_listener_on_click_move(self.make_move)
        self.__game_view.game_window.add_listener_on_click_sell(self.sell)
        self.__game_view.game_window.add_listener_on_click_build(self.build)

        self.__game_view.winner_window.add_listener_on_click_restart(self.restart)


        self.__game_view.loop()

    def run(self) -> None:
        count_players = self.__game_view.start_window.count_players.get()

        self.__game.set_up(count_players)

        name_cells = self.__game.board.get_name_cells()
        colors = self.__game.board.get_colors()

        self.__game_view.create_game_field(name_cells, colors, count_players)

        self.__game_view.start_window.start_loading()

        self.__game_view.show_present_window()

    def make_move(self) -> None:
        self.__game.make_move()

        self.__update_info()

        self.__game_view.update_idletasks()

        buying_permission = None

        if self.__game.board.is_ownerless(self.__game.get_current_cell()):
            buying_permission = MessageDropper.drop_message_ask(str(self.__game.get_current_cell()))

        elif not self.__game.board.is_free_parking(self.__game.get_current_cell()):
            MessageDropper.drop_message_info(str(self.__game.get_current_cell()))

        self.__game.processing_move(buying_permission)

        if self.__game.get_bankrupt_manager().is_bankrupt(self.__game.get_current_player().id):
            MessageDropper.drop_message_info("Игрок обанкротился \nи выбывает из игры 🚫")
            self.__game_view.game_window.delete_token(self.__game.get_current_player().id.get_value())

        if self.__game.get_winner_manager().is_winner():
            self.__game_view.show_winner_window(self.__game.get_current_player().id.get_value()+1)


    def restart(self) -> None:
        self.__game = Game()
        self.__game_view.show_start_window()


    def sell(self) -> None:
        pass


    def build(self) -> None:
        pass


    def __update_info(self) -> None:
        id = self.__game.get_current_player().id.get_value()
        balance = self.__game.get_current_balance()
        position = self.__game.get_current_player().get_position()
        points_1, points_2 = self.__game.get_current_points()
        ownership = self.__game.get_current_player().get_ownerships_names()

        self.__game_view.update_window(id, balance, position, points_1, points_2, ownership)





