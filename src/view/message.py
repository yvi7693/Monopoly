from typing_extensions import Literal
from tkinter.messagebox import askyesno, showinfo

from src.models.gameboard import *
from src.models.typescell import TypeMessage


class MessageDropper:

    def __init__(self):
        pass

    @staticmethod
    def drop_message_ask(name: str, price: int) -> bool:
        return askyesno(message=f"Желаете приобрести собственность?\n {name}: {price} $")

    @staticmethod
    def drop_message_info(type_message: Literal["positive", "negative", "jail"]):
        if type_message == "positive":
            showinfo(message=f"Вы попали на клетку шанс и получаете 200$")

        if type_message == "negative":
            showinfo(message=f"Вы попали на клетку шанс и вынуждены заплатить 200$")

        if type_message == "jail":
            showinfo(message=f"Вы попали в тюрьму и пропускаете ход")

