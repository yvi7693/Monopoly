from src.constant_view import WIDTH, HEIGHT
from src.controllers.core import Game
from src.presenter.sell_presenter import SellPresenter

from src.view.main_window import MainWindow
from src.view.message import MessageDropper
from src.view.windows_lower import SellWindow


class GamePresenter:

    __game: Game
    __game_view: MainWindow

    def __init__(self):
        self.__game = Game()
        self.__game_view = MainWindow(WIDTH, HEIGHT)

        self.__sell_window = None
        self.__sell_presenter = None

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

        self.update_info()
        self.update_place_token()

        self.__game_view.update_idletasks()

        buying_permission = None

        if self.__game.board.is_ownerless(self.__game.get_current_cell()):
            buying_permission = MessageDropper.drop_message_ask(self.__game_view, str(self.__game.get_current_cell()))

        elif not self.__game.board.is_free_parking(self.__game.get_current_cell()):
            MessageDropper.drop_message_info(self.__game_view, str(self.__game.get_current_cell()))

        self.__game.processing_move(buying_permission)

        if self.__game.get_bankrupt_manager().is_bankrupt(self.__game.get_current_player().id):
            MessageDropper.drop_message_info(self.__game_view, "Игрок обанкротился \nи выбывает из игры 🚫")
            self.__game_view.game_window.delete_token(self.__game.get_current_player().id.get_value())

        if self.__game.get_winner_manager().is_winner():
            self.__game_view.show_winner_window(self.__game.get_current_player().id.get_value()+1)

        self.update_info()

    def restart(self) -> None:
        self.__game = Game()
        self.__game_view.show_start_window()

    def sell(self) -> None:

        current_player = self.__game.get_current_player()

        if current_player is None:
            MessageDropper.drop_message_info(self.__game_view, "Нажмите MOVE для того чтобы определить текущего игрока.")
            return None

        if self.__sell_window is None or not self.__sell_window.winfo_exists():
            self.__sell_window = SellWindow(self.__game_view.game_window)

        else:
            self.__sell_window.focus()

        self.__sell_window.create_widgets(current_player.get_ownerships_names_list())
        self.__sell_presenter = SellPresenter(self.__game.get_manager_ownership(), self.__sell_window, self.__game, self.update_info)

        return None

    def build(self) -> None:
        pass

    def update_info(self) -> None:
        id = self.__game.get_current_player().id.get_value()
        balance = self.__game.get_current_balance()
        points_1, points_2 = self.__game.get_current_points()
        ownerships = self.__game.get_current_player().get_ownerships_names()

        self.__game_view.update_window_info(id, balance, points_1, points_2, ownerships)

    def update_place_token(self) -> None:
        id = self.__game.get_current_player().id.get_value()
        position = self.__game.get_current_player().get_position()

        self.__game_view.update_place_token(id, position)





