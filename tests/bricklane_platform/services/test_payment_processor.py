import unittest
from ..fixture import get_path


from bricklane_platform.services.payment_processor import PaymentProcessor
from bricklane_platform.models.card_payment import CardPayment


def create_stub_card_payment(mock_is_successful):
    payment = CardPayment()
    payment.is_successful = lambda: mock_is_successful
    return payment


class TestPaymentProcessor(unittest.TestCase):

    def setUp(self):
        self.payment_processor = PaymentProcessor()

    def test_get_card_payments(self):
        fixture = get_path("card_payments_mixed.csv")

        payments = self.payment_processor.get_payments(fixture, "card")
        self.assertEqual(len(payments), 3)
        self.assertEqual(payments[0].card.card_id, 30)
        self.assertEqual(payments[1].card.card_id, 45)
        self.assertEqual(payments[2].card.card_id, 10)

    def test_get_card_payments_empty(self):
        fixture = get_path("card_payments_empty.csv")

        payments = self.payment_processor.get_payments(fixture, "card")
        self.assertEqual(len(payments), 0)

    def test_verify_card_payments(self):
        payment1 = create_stub_card_payment(mock_is_successful=True)
        payment2 = create_stub_card_payment(mock_is_successful=False)
        payment3 = create_stub_card_payment(mock_is_successful=True)

        result = self.payment_processor.verify_payments([payment1, payment2, payment3])
        self.assertEqual(result, [payment1, payment3])

    def test_get_bank_payments(self):
        fixture = get_path("bank_payments_mixed.csv")

        payments = self.payment_processor.get_payments(fixture, "bank")
        self.assertEqual(len(payments), 2)
        self.assertEqual(payments[0].bank_account_id, 20)
        self.assertEqual(payments[1].bank_account_id, 60)

    def test_get_bank_payments_empty(self):
        fixture = get_path("bank_payments_empty.csv")

        payments = self.payment_processor.get_payments(fixture, "bank")
        self.assertEqual(len(payments), 0)
