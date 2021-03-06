from decimal import Decimal
from dateutil.parser import parse


from bricklane_platform.models.card import Card
from bricklane_platform.config import PAYMENT_FEE_RATE


class Payment(object):

    customer_id = None
    date = None
    amount = None
    fee = None

    def __init__(self, data=None):

        if not data:
            return

        self.customer_id = int(data["customer_id"])
        self.date = parse(data["date"])

        total_amount = Decimal(data["amount"])
        self.fee = total_amount * PAYMENT_FEE_RATE
        self.amount = total_amount - self.fee
