import unittest

from bricklane_platform.models.bank_payment import BankPayment


class TestBankPayment(unittest.TestCase):
    def test_init(self):
        bank_payment = BankPayment()

        self.assertIsNone(bank_payment.bank_account_id)

    def test_init_with_data(self):
        data = {
            "amount": "2000",
            "bank_account_id": "789",
            "customer_id": "123",
            "date": "2019-02-01",
        }

        bank_payment = BankPayment(data)

        self.assertEqual(bank_payment.bank_account_id, 789)
        self.assertEqual(bank_payment.amount, 1960)

    def test_is_successful(self):
        bank_payment = BankPayment()
        self.assertTrue(bank_payment.is_successful())
