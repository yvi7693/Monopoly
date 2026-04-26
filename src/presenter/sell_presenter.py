from typing import Callable

from src.controllers.core import Game
from src.controllers.purchasesale import ManagerOwnership
from src.models.gameboard import Street
from src.presenter.constant_presenter import SUCCESSFULLY_SELL_OWNERSHIP
from src.view.message import MessageDropper
from src.view.windows import GameWindow
from src.view.windows_lower import SellWindow


class SellPresenter:

    __manager_ownership: ManagerOwnership
    __sell_window: SellWindow
    __game: Game
    __game_window: GameWindow

    __callback_update: Callable
    __callback_move: Callable

    __need_sell: bool


    def __init__(self, manager_ownership: ManagerOwnership, sell_window: SellWindow | None, game: Game, callback_update: Callable, callback_move: Callable, need_sell: bool, game_window: GameWindow):

        self.__manager_ownership = manager_ownership
        self.__sell_window = sell_window
        self.__game = game
        self.__game_window = game_window

        self.__callback_update = callback_update
        self.__callback_move = callback_move

        self.__need_sell = need_sell

        self.__sell_window.add_listener_on_click_sell(self.sell)

    def sell(self) -> None:
        sell_index = self.__sell_window.get_sell_index()
        businessman = self.__game.get_current_player()

        ownership = businessman.ownerships[sell_index]

        self.__manager_ownership.sell_ownership(ownership, businessman.id)

        if isinstance(ownership, Street):
            self.__game_window.delete_builds(ownership.get_position())

        self.__game_window.delete_owner_label(ownership.get_position())

        self.__game.update_data()
        self.__game_window.update_idletasks()

        MessageDropper.drop_message_info(self.__sell_window, SUCCESSFULLY_SELL_OWNERSHIP + f"{ownership.get_name()}")

        self.__sell_window.close()

        if self.__need_sell:
            self.__callback_move()

