from abc import ABC, abstractmethod

"""
Клас продукту
"""
class Auto:
    def __init__(self, name):
        self.name = name
        self.body = None
        self.engine = None
        self.comfort = []


    def __str__(self):
        info: str = f"Pizza name: {self.name} \n" \

        return info

"""
Абстрактний клас задаючий інтерфейс будівельника
"""


class Builder(ABC):

    @abstractmethod
    def make_body (self) -> None: pass   #виготовити кузов авто

    @abstractmethod
    def add_engine(self) -> None: pass  #вставити двигун
    @abstractmethod
    def add_comfort(self) -> None: pass #добавити комплектацію комфорт

    @abstractmethod
    def get_auto(self) -> Auto: pass



"""
Реалізація конкретного монтувальника автомобіля
"""


class Passat_b6_builder(Builder):

    def __init__(self):
        self.auto = Auto("Passat_b6")

    def make_body(self) -> None:
        self.make_body = "Sedan"

    def add_engine(self) -> None:
        self.add_engine = "Disel 2"

    def add_comfort(self) -> None:
        self.add_comfort = ["Круїз", "Датчик дощу", "Підігрів сидінь"]
    def get_auto(self) -> Auto:
        return self.auto





"""
Клас Director, відповідає за поетапне виготовлення автомобіля
"""
class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_auto(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.make_body()
        self.builder.add_engine()
        self.builder.add_comfort()

if __name__ == '__main__':

    director = Director()
    for it in (Passat_b6_builder,):
        builder = it()
        director.set_builder(builder)
        director.make_auto()
        pizza = builder.get_auto()
        print(pizza)
        print('---------------------------')