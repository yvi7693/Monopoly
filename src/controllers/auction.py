from __future__ import annotations

from src.controllers.finance import Bank
from src.controllers.playermanager import PlayerManager
from src.models.gameboard import Ownership
from src.models.idbusinessman import IdBusinessman


class Auctioneer:

    START_PRICE = 10
    INCREMENT_BID = 20

    __player_manager: PlayerManager
    __bidding_terminal: BiddingTerminal

    def __init__(self, player_manager: PlayerManager, bank: Bank):

        self.__player_manager = player_manager
        self.__bank = bank
        self.__bidding_terminal = BiddingTerminal(bank)

        self.__lot = None

    def set_up(self, seller: IdBusinessman, lot: Ownership) -> None:

        participants = self.__player_manager.get_id_without_seller(seller)

        self.__bidding_terminal.set_up(participants)

        self.__lot = lot

    def try_end_auction(self) -> bool:
        if self.__bidding_terminal.check_winner():

            price = self.__bidding_terminal.get_price()

            winner = self.__bidding_terminal.get_highest_bidder()

            if not self.__bank.try_debit_account(price, winner):  raise AssertionError("У участника аукциона нет денег после выигрыша")

            self.__player_manager.add_ownership(self.__lot, winner)

            return True

        return False

    def __get_bidding_terminal(self) -> BiddingTerminal:
        return self.__bidding_terminal

    bidding_terminal = property(__get_bidding_terminal)


class BiddingTerminal:

    __highest_bidder: None | IdBusinessman

    def __init__(self, bank: Bank, participants: list[IdBusinessman] = None):

        self.__highest_bidder = None
        self.__price = Auctioneer.START_PRICE
        self.__bank = bank

        self.__participants = participants or []
        self.__queue = 0

        self.__bidder = None

    def set_up(self, participants: list[IdBusinessman]) -> None:
        self.__participants = participants

        self.__queue = 0

        self.__bidder = None
        self.__highest_bidder = None

        self.__price = Auctioneer.START_PRICE

        self.__set_current_bidder()

    def get_highest_bidder(self) -> IdBusinessman:
        return self.__highest_bidder

    def get_current_bidder(self) -> IdBusinessman:
        return self.__bidder

    def get_price(self) -> int:
        return self.__price

    def check_winner(self) -> bool:
        return len(self.__participants) == 1 and not self.__highest_bidder is None

    def try_place_bid(self) -> bool:

        next_bid = self.__price + Auctioneer.INCREMENT_BID

        if self.__bank.has_enough_money(next_bid, self.__bidder):

            self.__price = next_bid
            self.__highest_bidder = self.__bidder

            self.__set_current_bidder()

            return True

        self.skip_bid()

        return False

    def skip_bid(self) -> None:

        if self.__bidder == self.__highest_bidder:
            self.__highest_bidder = None

        self.__delete_participant()

        self.__set_current_bidder()

    def __set_current_bidder(self) -> None:
        count_bidder = len(self.__participants)

        self.__bidder = self.__participants[self.__queue]

        self.__queue += 1

        if self.__queue >= count_bidder:
            self.__queue = 0

    def __delete_participant(self) -> None:

        delete_index = None

        for i in range(len(self.__participants)):
            if self.__participants[i] == self.__bidder:
                delete_index = i

        if delete_index is None:  raise AssertionError("В списке нет искомого участника аукциона")

        self.__participants.pop(delete_index)

        if len(self.__participants) == 0:
            self.__queue = 0

        elif delete_index < self.__queue:
            self.__queue -= 1

        elif self.__queue >= len(self.__participants):
            self.__queue = 0








