import unittest

from email_parsing import find_sender_email

RAW_STRING = "Received: from x.y.test by example.netvia TCP with ESMTP id ABC12345" \
             "for <mary@example.net>;  21 Nov 1997 10:05:43 -0600\n" \
             "Received: from machine.example by x.y.test; 21 Nov 1997 10:01:22 -0600\n" \
             "From: John Doe <jdoe@machine.example>\n" \
             "To: Mary Smith <mary@example.net>\n" \
             "Subject: Saying Hello\n" \
             "Date: Fri, 21 Nov 1997 09:55:06 -0600\n" \
             "Message-ID: <1234@local.machine.example>\n"

RAW_STRING_NO_BRACKET = "From: John Doe jdoe@machine.example\n" \
             "To: Mary Smith <mary@example.net>\n"

RAW_STRING_NO_NAME = "From: jdoe@machine.example\n" \
             "To: Mary Smith <mary@example.net>\n"

RAW_STRING_MANY_NAME = "From: John Tim Apple Doe jdoe@machine.example\n" \
             "To: Mary Smith <mary@example.net>\n"


class TestEmailParser(unittest.TestCase):
    def setUp(self):
        self.email_original = RAW_STRING
        self.email_no_bracket = RAW_STRING_NO_BRACKET
        self.email_no_name = RAW_STRING_NO_NAME
        self.email_many_name = RAW_STRING_MANY_NAME

    def test_original(self):
        self.assertEqual(find_sender_email(self.email_original), ('John Doe', 'jdoe@machine.example'))

    def test_no_bracket(self):
        self.assertEqual(find_sender_email(self.email_no_bracket), ('John Doe', 'jdoe@machine.example'))

    def test_no_name(self):
        self.assertEqual(find_sender_email(self.email_no_name), ('', 'jdoe@machine.example'))

    def test_many_name(self):
        self.assertEqual(find_sender_email(self.email_many_name), ('John Tim Apple Doe', 'jdoe@machine.example'))


if __name__ == "__main__":
    unittest.main()
