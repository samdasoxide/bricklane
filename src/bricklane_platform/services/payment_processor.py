import csv

from bricklane_platform.models.card_payment import CardPayment
from bricklane_platform.models.bank_payment import BankPayment


class PaymentProcessor(object):

    def get_payments(self, csv_path, source):
        payments = []
        with open(csv_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                if source == 'card':
                    payments.append(CardPayment(row))
                if source == 'bank':
                    payments.append(BankPayment(row))

        return payments

    def verify_payments(self, payments):
        successful_payments = []
        for payment in payments:
            if payment.is_successful():
                successful_payments.append(payment)

        return successful_payments
