class Customer:
    def __init__(self, name):
        self.name = name
        # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
        self.__discount = 10

    def get_price(self, price: float) -> float:
        return float(round(price * (1 - self.__discount / 100), 2))

    def set_discount(self, new_discount):
        if new_discount > 80:
            self.__discount = 80
        else:
            self.__discount = new_discount


customer = Customer("Иван Иванович")
print(customer.get_price(100))
customer.set_discount(20)
customer.get_price(100)
