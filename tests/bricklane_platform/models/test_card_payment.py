import unittest

from bricklane_platform.models.card_payment import CardPayment
from bricklane_platform.models.card import Card


class TestCardPayment(unittest.TestCase):
    def test_init(self):
        card_payment = CardPayment()

        self.assertIsNone(card_payment.card)

    def test_init_with_data(self):
        data = {
            "amount": "2000",
            "card_id": "45",
            "card_status": "processed",
            "customer_id": "123",
            "date": "2019-02-01",
        }

        card_payment = CardPayment(data)
        card = card_payment.card

        self.assertIsInstance(card, Card)
        self.assertEqual(card.card_id, 45)
        self.assertEqual(card_payment.amount, 1960)
        self.assertEqual(card.status, "processed")

    def test_is_successful(self):
        card = Card()
        card.status = "processed"
        card_payment = CardPayment()
        card_payment.card = card

        self.assertTrue(card_payment.is_successful())

    def test_is_successful_declined(self):
        card = Card()
        card.status = "declined"
        card_payment = CardPayment()
        card_payment.card = card

        self.assertFalse(card_payment.is_successful())

    def test_is_successful_errored(self):
        card = Card()
        card.status = "errored"
        card_payment = CardPayment()
        card_payment.card = card

        self.assertFalse(card_payment.is_successful())
