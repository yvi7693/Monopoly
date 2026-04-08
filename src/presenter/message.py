from src.controllers.tokenplacer import TokenPlacer
from src.view.message import MessageDropper


class MessagePresenter:

    def __init__(self, token_placer: TokenPlacer, message_dropper: MessageDropper):

        self.__token_placer = token_placer
        self.__message_dropper = message_dropper

