from abc import abstractmethod


class TurnTicket:
    def __init__(self, turn_number):
        self.turn_number = turn_number


class ITurnNumberSequence:
    @staticmethod
    @abstractmethod
    def next_turn_number():
        pass


class TurnNumberSequence(ITurnNumberSequence):
    _turn_number = -1

    @staticmethod
    def next_turn_number():
        TurnNumberSequence._turn_number += 1
        return TurnNumberSequence._turn_number


class TicketDispenser:
    def __init__(self, ):
        pass

    def get_turn_ticket(self):
        new_turn_number = ITurnNumberSequence.next_turn_number()
        return TurnTicket(new_turn_number)
