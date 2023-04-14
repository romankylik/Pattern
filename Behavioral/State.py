from abc import ABC, abstractmethod
from enum import Enum
from random import choice
from typing import List


class OrderState(Enum):
    """ТМожливі стани онлайн замовлення, Ключі стану"""
    MAKE_ORDER = 2  #
    AWAITING_PAY = 1  # Очікує оплати
    SEND_ORDER = 3  #Передано перевізнику

class OnlineShop:
    """Клас онлайн магазину"""
    def __init__(self):
        self.money: int = 0
        self.__states: dict[OrderState, State] = {
            OrderState.MAKE_ORDER: MAKE_ORDER_State(),
            OrderState.AWAITING_PAY: AWAITING_PAY_State(),
            OrderState.SEND_ORDER: SEND_ORDER_State()
        }
        self.__now_state: State = self.__states[OrderState.MAKE_ORDER]


    def get_state(self):
        return self.__now_state

    def set_state(self, state: 'State'):
        self.__now_state = self.__states[state]

    def insert_money(self, money: int) -> None:
        self.money += money
        print(f"Внесено {self.money} гривень")
        self.__now_state.insert_money(self)

    def make_order(self) -> None:
        self.__now_state.make_order(self)

    def end_shoping(self) -> None:
        self.__now_state.send_order(self)


class State(ABC):
    """Базовий клас стану, визначаючий інтерфейс"""
    @abstractmethod
    def make_order(self, coffee_machine) -> None:  #Зробити замовлення
        ...
    @abstractmethod
    def insert_money(self, coffee_machine) -> None:  #Очікує оплати
        ...
    @abstractmethod
    def send_order(self, coffee_machine) -> None:  #Відправляє замовлення
        ...
    def __str__(self):
        return self.__class__.__name__

class MAKE_ORDER_State(State):
    """Стан оформлення замовлення"""
    def make_order(self, online_shop) -> None:
        cost = 105 #Вартість товару
        print(f"Дякуємо за замовлення, очікуємо оплати {cost}грн")
        online_shop.set_state(OrderState.AWAITING_PAY)
    def insert_money(self, coffee_machine) -> None:
        print("Кошти отримано, та ви не вибрали товар")

    def send_order(self, coffee_machine) -> None:
        print("Оберіть товар!!!")

class AWAITING_PAY_State(State):
    """Стан очікування оплати"""

    def make_order(self, coffee_machine) -> None:
        cost = 307  # Вартість товару
        print(f"Вирішили обрати інший товар, попереджаємо його вартість {cost}грн")

    def insert_money(self, coffee_machine) -> None:
        cost = 105
        if coffee_machine.money >= cost:
            print("Кошти отримано, передаємо товар перевізнику")
            coffee_machine.set_state(OrderState.SEND_ORDER)
            coffee_machine.end_shoping()
        else:
            print("Недостатньо коштів")

    def send_order(self, coffee_machine) -> None:
        print("Нажаль ми не можемо відправити товар поки не буде внесено коштів")


class SEND_ORDER_State(State):
    """Стан завершення покупки, відправка товару покупцеві."""

    def make_order(self, coffee_machine) -> None:
        print(f"Поточну покупку завершено, добавте новий товар в корзину")

    def insert_money(self, coffee_machine) -> None:
        print("Кошти отримано. У вас надлишок коштів, вони зберігатимуться на вашому рахунку")


    def send_order(self, coffee_machine) -> None:
        print("Дякуємо за покупку, товар уже прямує до вас")

if __name__ == "__main__":
    online_shop = OnlineShop()
    print(f"____поточний стан:  {online_shop.get_state()}")
    online_shop.make_order()
    print(f"____поточний стан:  {online_shop.get_state()}")
    online_shop.insert_money(68)
    print(f"____поточний стан:  {online_shop.get_state()}")
    online_shop.insert_money(200)
    print(f"____поточний стан:  {online_shop.get_state()}")
