from abc import ABC, abstractmethod
from enum import Enum
from random import choice
from typing import List


class OrderType(Enum):
    """Типи можливих замовлень додатку онлайн магаз."""
    CLOTHES = 1
    TECHNICS = 2
    BOOKS = 3


class Order:
    """Клас замовлення"""
    order_id: int = 1

    def __init__(self, order_type: OrderType):
        self.id = Order.order_id
        self.type = order_type
        Order.order_id += 1

    def __str__(self):
        return f"Замовлення під №{self.id} ({self.type.name})"


class Observer(ABC):
    @abstractmethod
    def update(self, order_id: int):
        ...


class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []  #Список з спостерігачів (покупців)

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, order_id: int) -> None:
        for observer in self._observers:
            observer.update(order_id)


class OnlineShop(Subject):
    def __init__(self):
        super().__init__()
        self.__orders: List[Order] = []           #нові замовлення в магазині
        self.__arrived_buyer_order: List[Order] = []   #замовлення які прибули до покупця та очікують коли їх заберуть

    def take_order(self, order: Order) -> None:
        print(f"Фіксуємо нову покупку {order}")
        self.__orders.append(order)

    def get_order(self, order_id: int) -> Order:   #забрати замовлення покупцем
        order = None
        for it in self.__arrived_buyer_order:
            if it.id == order_id:
                order = it
                break
        self.__arrived_buyer_order.remove(order)
        return order

    def delivery_order(self):                      #Доставка товару до клієнта
        if self.__orders:
            one_order = choice(self.__orders)
            self.__orders.remove(one_order)
            self.__arrived_buyer_order.append(one_order)
            print(f"Замовлення прибуло до покупця {one_order}")
            self.notify(one_order.id)



class Buyer(Observer):
    def __init__(self, name: str, shop: OnlineShop):
        self.__shop = shop
        self.__name = name
        self.order: Order = None

    def update(self, order_id: int) -> None:
        """Приймає номер замовлення, яке прибуло та
                відписується від відстежування замовлення"""
        if self.order is not None:
            if order_id == self.order.id:
                print(f"Клієнт {self.__name} забрав(ла) "
                      f"{self.__shop.get_order(order_id)}")
                self.__shop.detach(self)

    def create_order(self) -> None:
        """Метод на створення покупки та підписка на відстеження покупки"""
        order_type = choice([OrderType.CLOTHES,
                             OrderType.TECHNICS,
                             OrderType.BOOKS])
        self.order = Order(order_type)
        print(f"Клієнт {self.__name} замовив {self.order}")
        self.__shop.attach(self)
        self.__shop.take_order(self.order)


if __name__ == "__main__":
    names = ['Анастасія', 'Анна',
             'Роман', 'Ростислав', 'Руслан']
    shop = OnlineShop()
    clients = [Buyer(name, shop) for name in names]
    for client in clients:
        client.create_order()
        print("-" * 5)
    print("_" * 4 + "Магазин відправив товар покупцеві" + 4 * "_")
    for _ in range(5):
        print("*"*30)
        shop.delivery_order()