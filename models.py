class Fish:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def info(self):
        return f"Fish: {self.name}, Price: {self.price}G"
