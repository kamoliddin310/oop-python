class BankAck:
    __balans = 0

    def __init__(self, name) -> None:
        self.name = name

    def get_b(self)-> float:
        return self.__balans
    
    # setter
    def deposit(self, money: float)-> None:
        self.__balans += money

    def withdraw(self, money: float)-> None:
        if money > 0 and self.__balans >= money:
            self.__balans -= money

ba = BankAck("Ali")
print(ba.get_b())