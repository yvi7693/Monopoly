from tkinter.messagebox import askyesno, showinfo

class MessageDropper:

    def __init__(self):
        pass

    @staticmethod
    def drop_message_ask(parent, message: str) -> bool:
        return askyesno(parent=parent, message=f"Желаете приобрести собственность?\n {message}")

    @staticmethod
    def drop_message_info(parent, message: str):
        return showinfo(parent=parent, message=f"{message}")

