from src.controllers.auction import Auctioneer
from src.controllers.finance import Bank
from src.models.gameboard import Ownership
from src.models.idbusinessman import IdBusinessman
from src.view.message import MessageDropper
from src.view.windows_lower import AuctionWindow


class AuctionPresenter:

    __auctioneer: Auctioneer
    __auction_window: AuctionWindow

    def __init__(self, auctioneer: Auctioneer, auction_window: AuctionWindow, seller: IdBusinessman, lot: Ownership, bank: Bank):
        self.__auctioneer = auctioneer
        self.__auction_window = auction_window

        self.__bank = bank

        self.__auction_window.add_listener_on_click_bid(self.place_bid)
        self.__auction_window.add_listener_on_click_skip(self.skip_bid)

        self.__auctioneer.set_up(seller, lot)

        bidder = self.__auctioneer.bidding_terminal.get_current_bidder()

        self.__auction_window.create_widgets(lot.get_name(), Auctioneer.START_PRICE, bidder.get_value()+1, self.__bank.get_balance(bidder), Auctioneer.INCREMENT_BID)

    def place_bid(self) -> None:

        if not self.__auctioneer.bidding_terminal.try_place_bid():

            MessageDropper.drop_message_info(self.__auction_window, "У игрока не достаточно средств, чтобы подтвердить ставку")
            MessageDropper.drop_message_info(self.__auction_window, "Игрок выбывает из аукциона, так как не подтвердил ставку")

        self.__try_end_auction()

        self.update_window()

        return None

    def skip_bid(self) -> None:
        self.__auctioneer.bidding_terminal.skip_bid()

        MessageDropper.drop_message_info(self.__auction_window, "Игрок выбывает из аукциона, так как не подтвердил ставку")

        if self.__try_end_auction():
            return None

        self.update_window()

        return None

    def update_window(self) -> None:
        bidder = self.__auctioneer.bidding_terminal.get_current_bidder()
        price = self.__auctioneer.bidding_terminal.get_price()
        balance = self.__bank.get_balance(bidder)

        self.__auction_window.update_widgets(price, bidder.get_value()+1, balance)

    def __try_end_auction(self) -> bool:

        if self.__auctioneer.try_end_auction():
            MessageDropper.drop_message_info(self.__auction_window, "Аукцион завершен")

            self.__auction_window.destroy()

            return True

        return False
