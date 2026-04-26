from tkinter.messagebox import askyesno, showinfo

from src.view.constant_view import WANT_BUY


class MessageDropper:

    def __init__(self):
        pass

    @staticmethod
    def drop_message_ask(parent, message: str) -> bool:
        return askyesno(parent=parent, message=WANT_BUY + f"\n {message}")

    @staticmethod
    def drop_message_info(parent, message: str):
        return showinfo(parent=parent, message=f"{message}")

