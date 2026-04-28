from datetime import datetime

class Sale:

    def __init__(self, detail):
        self.detail = detail
        self.date = datetime.now()

    def to_dict(self):
        return vars(self)