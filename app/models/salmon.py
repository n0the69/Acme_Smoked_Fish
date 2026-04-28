class Salmon:

    def __init__(self, name, cost, price, stock):
        self.name = name
        self.cost = cost
        self.price = price
        self.stock = stock

    def to_dict(self):
        return vars(self)