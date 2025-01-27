from datetime import datetime


class CardType:
    def __init__(self, name: str) -> None:
        self.name = name


class Card:
    def __init__(self, name: str, number: int, cvv: int, exapry_date: datetime, money: float, type: CardType):
        self.name = name
        self.number = number
        self.cvv = cvv
        self.expary_date = exapry_date
        self.money = money
        self.type = type


class AloqaBankCard(Card):
    pass


class NBUBankCard(Card):
    pass


class SQBBankCard(Card):
    pass


class Account:
    __cards: list[Card] = []

    def __init__(self, first_name: str, last_name: str, phone: str) -> None:
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.phone = phone
    
    def add_card(self, card: Card) -> None:
        self.__cards.append(card)

    def get_balans(self) -> float:
        s = 0
        for card in self.__cards:
            s += card.money

        return s


types = [CardType("Humo"), CardType("Uzcard"), CardType("Visa")] 


account = Account("ali", "vali", "+998881234567")
c1 = AloqaBankCard('olyik', 2345123451234123, 566, datetime(2029, 12, 12), 1200000, types[0])
c2 = SQBBankCard('bissness', 4132413241234, 435, datetime(2030, 12, 12), 235400000, types[2])

account.add_card(c1)
account.add_card(c2)

print(account.get_balans())
