from src.controllers.building import Builder
from src.controllers.core import Game
from src.models.building import BuildingTypes
from src.view.message import MessageDropper
from src.view.windows_lower import BuildWindow


class BuildPresenter:

    def __init__(self, builder: Builder, build_window: BuildWindow | None, game: Game, callback_update):
        self.__builder = builder
        self.__build_window = build_window
        self.__game = game

        self.__callback_update = callback_update

        self.__build_window.add_listener_on_click_home(self.build_home)
        self.__build_window.add_listener_on_click_hotel(self.build_hotel)

    def build_home(self) -> None:
        build_index = self.__build_window.get_build_index()

        businessman = self.__game.get_current_player()

        if self.__builder.try_build(businessman.id, businessman.get_street()[build_index], BuildingTypes.HOME):
            MessageDropper.drop_message_info(self.__build_window, "Вы построили дом")

        else:
            MessageDropper.drop_message_info(self.__build_window, "Не удалось построить дом")

        self.__game.update_data()
        self.__callback_update()

    def build_hotel(self) -> None:
        build_index = self.__build_window.get_build_index()

        businessman = self.__game.get_current_player()

        if self.__builder.try_build(businessman.id, businessman.get_street()[build_index], BuildingTypes.HOTEL):
            MessageDropper.drop_message_info(self.__build_window, "Вы построили отель")

        else:
            MessageDropper.drop_message_info(self.__build_window, "Не удалось построить отель")

        self.__game.update_data()
        self.__callback_update()