from abc import ABC, abstractmethod

class Payments(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPIPayment(Payments):
    def pay(self, amount):
        print(f"Paid {amount} by UPI")


class NetBanking(Payments):
    def pay(self, amount):
        print(f"Paid {amount} by Net Banking")


class Card(Payments):
    def pay(self, amount):
        print(f"Paid {amount} by debit card")


p1 = UPIPayment()
p1.pay(1000)

