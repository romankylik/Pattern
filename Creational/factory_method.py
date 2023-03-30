from abc import *

"""Інтерфейс для виготовлення продукту"""
class Product:
    def __init__(self):
        self.type = ""

    def __str__(self) -> str:
        return self.type

"""Конкретний продукт"""
class  PlaneProduct(Product):
    def __init__(self):
        self.type = "Plane"
    def __str__(self) -> str:
        return self.type

class  TankProduct(Product):
    def __init__(self):
        self.type_pr = "Tank"
    def __str__(self) -> str:
        return self.type_pr


"""Інтерфейс фабрики (творець) із фабричним методом."""
class Creator():
    @abstractmethod
    def factory_method(self, product_type: Product) -> Product:

        pass
    @abstractmethod
    def some_logik (self):
        """Певна логіка творця, та виклик фабричного методу"""
        return self.factory_method()
    def __str__(self):
        return f'Фабрика створила {self.some_logik()}'


class FactoryTank(Creator):
    def factory_method(self) -> Product:
        return TankProduct()

    def some_logik (self):
        """Певна логіка творця, та виклик фабричного методу"""
        return self.factory_method()
    def __str__(self):
        return f'Фабрика створила {self.some_logik()}'

class FactoryPlane(Creator):
    def factory_method(self) -> Product:
        return PlaneProduct()

    def some_logik (self):
        """Певна логіка творця, та виклик фабричного методу"""
        return self.factory_method()

    def __str__(self):
        return f'Фабрика створила {self.some_logik()}'


def client_code(creator: str) -> None:
    creators = {
        "T": FactoryTank,
        "P": FactoryPlane
    }
    return creators[creator]()

if __name__ == '__main__':
    new = client_code('P')
    print (new)

"""Було створено інтерфейс продукту та його екземпляри - конкретні продукти (TankProduct, PlaneProduct). 
Також створено інтевфейс для Creator(творця продутків), та від повідні творці для конкретних продуктів, із фабричними методами які повертають нам конкретні продукти.
Також створена метод клієнського коду , якому ми кажемо який нам продукт потрібен,  а він нам повертає -> Творця продукту -> Сам продукт.
 
 
Оскільки мінусом цього паттерна є велика кількість класів творців( для кожного продутку потрібен свій творець).
Тому на попередньому уроці я показував один клас творця без його інтерфейсу, який повертав нам потрібний продукт(необхідний продукт задавався в клієнському коді)."""


