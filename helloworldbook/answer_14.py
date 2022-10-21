class BankAccount():
    def __init__(self, name, id, balance):
        self.name = name
        self.id = id
        self.balance = balance

    def get_balance(self):
        print("您的账户余额为："+str(self.balance))

    def save_money(self, money):
        self.balance += money
        print("存钱成功！您的余额为："+str(self.balance))

    def get_money(self, money):
        if (money > self.balance):
            print("您的余额不足！")
        else:
            self.balance -= money
            print("取钱成功！您的余额为："+str(self.balance))


class InterestAccount(BankAccount):
    def __init__(self):
        self.rate = 0.1

    def raise_rate(self, value):
        self.rate += value

    def addInterest(self):
        self.balance *= 1 + self.rate


user1 = BankAccount('user1', 1, 500)
user1.get_balance()
user1.get_money(1000)
user1.get_money(500)
user1.save_money(10000)
