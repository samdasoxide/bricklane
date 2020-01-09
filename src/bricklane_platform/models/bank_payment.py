from payment import Payment


class BankPayment(Payment):
    bank_account_id = None

    def __init__(self, data=None):
        if not data:
            return

        super(BankPayment, self).__init__(data)
        self.bank_account_id = int(data["bank_account_id"])

    def is_successful(self):
        return True
