from __future__ import annotations

from src.controllers.finance import Bank
from src.controllers.playermanager import PlayerManager
from src.models.gameboard import Ownership
from src.models.idbusinessman import IdBusinessman


class Auctioneer:

    START_PRICE = 10
    INCREMENT_BID = 20

    __player_manager: PlayerManager
    __bank: Bank

    __bidding_terminal: BiddingTerminal
    __queue_manager: QueueManager

    __lot: Ownership | None


    def __init__(self, player_manager: PlayerManager, bank: Bank):

        self.__player_manager = player_manager
        self.__bank = bank

        self.__queue_manager = QueueManager()
        self.__bidding_terminal = BiddingTerminal(bank, self.__queue_manager)

        self.__lot = None

    def set_up(self, seller: IdBusinessman, lot: Ownership) -> None:

        participants = self.__player_manager.get_id_without_seller(seller)

        self.__queue_manager.set_up(participants)

        self.__bidding_terminal.set_price(Auctioneer.START_PRICE)

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

    def __get_queue_manager(self) -> QueueManager:
        return self.__queue_manager

    bidding_terminal = property(__get_bidding_terminal)
    queue_manager = property(__get_queue_manager)


class BiddingTerminal:

    __highest_bidder: None | IdBusinessman
    __price: int

    __bank: Bank

    __queue_manager: QueueManager

    def __init__(self, bank: Bank, queue_manager: QueueManager):

        self.__price = Auctioneer.START_PRICE
        self.__bank = bank
        self.__queue_manager = queue_manager

        self.__highest_bidder = None

    def get_price(self) -> int:
        return self.__price

    def set_price(self, new_price: int) -> None:
        self.__price = new_price

    def get_highest_bidder(self) -> IdBusinessman:
        return self.__highest_bidder

    def check_winner(self) -> bool:
        participants = self.__queue_manager.get_participants()

        return len(participants) == 1 and not self.__highest_bidder is None

    def check_all_skip(self) -> bool:
        participants = self.__queue_manager.get_participants()

        return len(participants) == 0 and self.__highest_bidder is None

    def try_place_bid(self) -> bool:

        next_bid = self.__price + Auctioneer.INCREMENT_BID

        if self.__bank.has_enough_money(next_bid, self.__queue_manager.current_bidder):

            self.__price = next_bid
            self.__highest_bidder = self.__queue_manager.current_bidder

            self.__queue_manager.next_bidder()

            return True

        self.skip_bid()

        return False

    def skip_bid(self) -> None:

        if self.__queue_manager.current_bidder == self.__highest_bidder:
            self.__highest_bidder = None

        if self.check_all_skip():
            return None

        self.__queue_manager.delete_current_bidder()

        if not self.check_all_skip():
            self.__queue_manager.next_bidder()

        return None


class QueueManager:

    __participants: list[IdBusinessman]

    __queue: int

    __bidder: IdBusinessman | None

    def __init__(self, participants: list[IdBusinessman] = None):
        self.__participants = participants or []

        self.__queue = 0

        self.__bidder = None

    def get_participants(self) -> list[IdBusinessman]:
        return self.__participants

    def set_up(self, participants: list[IdBusinessman]) -> None:
        self.__participants = participants

        self.__queue = 0

        self.__bidder = None

        self.next_bidder()

    def next_bidder(self) -> None:
        count_bidder = len(self.__participants)

        self.__bidder = self.__participants[self.__queue]

        self.__queue += 1

        if self.__queue >= count_bidder:
            self.__queue = 0

    def delete_current_bidder(self) -> None:

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

    def __get_current_bidder(self) -> IdBusinessman:
        return self.__bidder

    current_bidder = property(__get_current_bidder)










