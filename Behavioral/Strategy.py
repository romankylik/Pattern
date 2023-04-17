from abc import ABC, abstractmethod


class Strategy(ABC):
    """Интерфейс стратегии"""
    cost = 0
    time_delivery = 0
    name = ""

    def get_cost(self):
        ...

    def get_time(self):
        ...
    def __str__(self):
        return f"Вибрано тип доставки: {self.name}, його доставлять протягом {self.get_time()} днів"


class NovaPoshtaStrategy(Strategy):
    def __init__(self, cost):
        self.cost = cost
        self.time_delivery = 1
        self.name = "Нова Пошта"
    def get_cost(self):
        return self.cost

    def get_time(self):
        return self.time_delivery



class UKRPoshtaStrategy(Strategy):
    def __init__(self, cost):
        self.cost = cost
        self.time_delivery = 3
        self.name = "Укр пошта"
    def get_cost(self):
        return self.cost

    def get_time(self):
        return self.time_delivery


class SelfPickup(Strategy):
    def __init__(self, cost):
        self.cost = cost
        self.time_delivery = 5
        self.name = "Самовивіз"
    def get_cost(self):
        return self.cost

    def get_time(self):
        return self.time_delivery

    def __str__(self):
        return f"Вибрано тип доставки: {self.name}, його можна отримати протягом {self.get_time()} днів"


class Order:
    def __init__(self, type_order, cost_order, delivery: Strategy):
        self.type = type_order
        self.cost = cost_order
        self._strategy = delivery

    def set_delivery(self, delivery):
        self._strategy = delivery

    def __str__(self):
        return f""" Дякуємо що замовили {self.type}, його вартість разом із доставкою {self.cost + self._strategy.get_cost()}$
 {self._strategy}
 """



if __name__ == "__main__":
    new_order = Order("Телефон", 50, NovaPoshtaStrategy(2))
    print(new_order)
    print("-" * 5)
    order2 = Order("Books", 20, UKRPoshtaStrategy(1))
    print(order2)
    print("-" * 5)

    # Клієнт передумав та вирішив забрати самостійно товар з магазину
    order2.set_delivery(SelfPickup(0))
    print(order2)
    print("-" * 5)