from tkinter.messagebox import askyesno, showinfo

class MessageDropper:

    def __init__(self):
        pass

    @staticmethod
    def drop_message_ask(message: str) -> bool:
        return askyesno(message=f"Желаете приобрести собственность?\n {message}")

    @staticmethod
    def drop_message_info(message: str):
        return showinfo(message=f"{message}")

