from abc import ABC, abstractmethod
from typing import List


class Visitor:
    """Клас відвідувач один, та має окремий метод для різних обєктів(товарів)"""

    def visit_clothing(self, clothing):
        return clothing.price * 0.25

    def visit_books(self, books):
        return books.price * 0.25


    def visit_electronics(self, electronics):
        return electronics.price * 0.25


class Element(ABC):
    """Інтерфейс продукту"""
    @abstractmethod
    def accept(self, visitor: Visitor) -> float:
        ...

class Clothing(Element):
    """Клас обєкту Одяг"""
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

    def accept(self, visitor):
        return visitor.visit_clothing(self)

class Book(Element):
    """Клас обєкту книги"""
    def __init__(self, name: str, price: float, author: str):
        self.name = name
        self.price = price
        self.author = author

    def accept(self, visitor: Visitor) -> float:
        return visitor.visit_books(self)

class Electronics(Element):
    """Клас обєкту електроніка"""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def accept(self, visitor):
        return visitor.visit_electronics(self)

def all_cost(orders: List, date = 0)-> float:
    visitor = Visitor()
    cost = 0
    if date == 13:
        for product in orders:
            cost += product.accept(visitor)
    else:
        for product in orders:
            cost += product.price
    return cost

if __name__ == "__main__":
    # Створення продуктів
    iphone = Electronics("iPhone", 1000)
    tshirt = Clothing("T-Shirt", 20, "M")
    book = Book("The Alchemist", 10, "Paulo Coelho")

    # Створення замовлення
    order = [iphone, tshirt, book]

    # Обчислення вартості замовлення без знижки
    total_cost = all_cost(order)
    print(f"Загальна вартість без знижки - {total_cost} грн")

    # Обчислення вартості замовлення зі знижкою 25% в пятницю 13
    total_cost = all_cost(order, 13)
    print(f"Загальна вартість в пятницю 13, зі знижкою 25% - {total_cost} грн.")