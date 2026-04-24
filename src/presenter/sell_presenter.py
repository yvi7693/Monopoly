from src.controllers.core import Game
from src.controllers.purchasesale import ManagerOwnership
from src.models.gameboard import Street
from src.view.message import MessageDropper
from src.view.windows import GameWindow
from src.view.windows_lower import SellWindow


class SellPresenter:

    def __init__(self, manager_ownership: ManagerOwnership, sell_window: SellWindow | None, game: Game, callback_update, game_window: GameWindow):

        self.__manager_ownership = manager_ownership
        self.__sell_window = sell_window
        self.__game = game
        self.__game_window = game_window

        self.__callback_update = callback_update

        self.__sell_window.add_listener_on_click_sell(self.sell)

    def sell(self) -> None:
        sell_index = self.__sell_window.get_sell_index()
        businessman = self.__game.get_current_player()

        ownership = businessman.ownerships[sell_index]

        self.__manager_ownership.sell_ownership(ownership, businessman.id)

        if isinstance(ownership, Street):
            self.__game_window.delete_builds(ownership.get_position())

        self.__game_window.delete_owner_label(ownership.get_position())

        MessageDropper.drop_message_info(self.__sell_window, message=f"Вы продали собственность {ownership.get_name()}")

        self.__game.update_data()
        self.__callback_update()

        self.__sell_window.close()