from src.controllers.core import Game
from src.view.windows import MainWindow

class GamePresenter:

    def __init__(self):
        self.__game = Game()
        self.__game_view = MainWindow(600, 500)

        self.__game_view.add_listener_on_click_start(self.run)

        self.__game_view.loop()

    def run(self):
        print("KArakararakra")


GamePresenter()
