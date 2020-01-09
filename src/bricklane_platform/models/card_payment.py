from payment import Payment
from card import Card


class CardPayment(Payment):
    card = None

    def __init__(self, data=None):
        if not data:
            return

        super(CardPayment, self).__init__(data)
        card = Card()
        card.card_id = int(data["card_id"])
        card.status = data["card_status"]
        self.card = card

    def is_successful(self):
        return self.card.status == "processed"
