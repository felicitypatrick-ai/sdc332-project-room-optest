import unittest

from app.notices import notice_message


class MessageTests(unittest.TestCase):
    def test_message_names_who_and_time(self):
        text = notice_message("Robins", "14:00")
        self.assertIn("Robins", text)
        self.assertIn("14:00", text)
