import unittest
from unittest.mock import patch

from turn_ticket import TicketDispenser


class TicketDispenserTest(unittest.TestCase):
    @patch("turn_ticket.ITurnNumberSequence")
    @patch("turn_ticket.TurnTicket")
    def test_ticket_dispenser(self, turn_ticket, turn_num_seq):
        turn_num_seq.next_turn_number.return_value = 10
        dispenser = TicketDispenser()
        dispenser.get_turn_ticket()
        turn_ticket.assert_called_with(10)

        turn_num_seq.next_turn_number.return_value += 1
        dispenser_2 = TicketDispenser()
        dispenser_2.get_turn_ticket()
        turn_ticket.assert_called_with(11)


if __name__ == "__main__":
    unittest.main()
