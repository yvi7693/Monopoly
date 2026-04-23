from src.controllers.building import Builder
from src.controllers.core import Game
from src.models.building import BuildingTypes
from src.view.message import MessageDropper
from src.view.windows import GameWindow
from src.view.windows_lower import BuildWindow


class BuildPresenter:

    def __init__(self, builder: Builder, build_window: BuildWindow | None, game: Game, callback_update, game_window: GameWindow):
        self.__builder = builder
        self.__build_window = build_window
        self.__game = game
        self.__game_window = game_window

        self.__callback_update = callback_update

        self.__build_window.add_listener_on_click_home(self.build_home)
        self.__build_window.add_listener_on_click_hotel(self.build_hotel)

    def build_home(self) -> None:
        build_index = self.__build_window.get_build_index()

        businessman = self.__game.get_current_player()
        street = businessman.get_streets()[build_index]

        if self.__builder.try_build(businessman.id, street, BuildingTypes.HOME):
            self.__game_window.create_home(street.get_position(), street.get_count_build() - 1)

            MessageDropper.drop_message_info(self.__build_window, "Вы построили дом")

        else:
            MessageDropper.drop_message_info(self.__build_window, "Не удалось построить дом")

        self.__game.update_data()
        self.__callback_update()

    def build_hotel(self) -> None:
        build_index = self.__build_window.get_build_index()

        businessman = self.__game.get_current_player()

        street = businessman.get_streets()[build_index]

        if self.__builder.try_build(businessman.id, street, BuildingTypes.HOTEL):
            self.__game_window.create_hotel(street.get_position())
            MessageDropper.drop_message_info(self.__build_window, "Вы построили отель")

        else:
            MessageDropper.drop_message_info(self.__build_window, "Не удалось построить отель")

        self.__game.update_data()
        self.__callback_update()