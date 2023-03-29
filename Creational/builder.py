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
        info: str = f"Auto name: {self.name} \n" \
                    f"body type: {self.body} \n" \
                    f"engine type: {self.engine} \n" \
                    f"comfort: {self.comfort}"

        return info

"""
Абстрактний клас задаючий інтерфейс будівельника
"""


class Builder(ABC):

    @abstractmethod
    def make_body (self) -> None: pass   #кузов авто

    @abstractmethod
    def add_engine(self) -> None: pass  # двигун
    @abstractmethod
    def add_comfort(self) -> None: pass #добавити комплектацію комфорт

    @abstractmethod
    def get_auto(self) -> Auto: pass



"""
Реалізація конкретного монтувальника автомобіля 1
"""


class Passat_b6_builder(Builder):

    def __init__(self):
        self.auto = Auto("Passat_b6")

    def make_body(self) -> None:
        self.auto.body = "Sedan"

    def add_engine(self) -> None:
        self.auto.engine = "Disel 2.0"
    def add_comfort(self) -> None:
        self.auto.comfort = ["Круїз", "Датчик дощу", "Підігрів сидінь"]
    def get_auto(self) -> Auto:
        return self.auto


"""
Реалізація конкретного монтувальника автомобіля 2
"""


class Skoda_Fabia_builder(Builder):

    def __init__(self):
        self.auto = Auto("Skoda Fabia")

    def make_body(self) -> None:
        self.auto.body = "Comby"

    def add_engine(self) -> None:
        self.auto.engine = "Gas 1.4"
    def add_comfort(self) -> None:
        self.auto.comfort = ["Клімат контроль", "Круїз", "Датчик дощу", "Підігрів сидінь"]
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
    for it in (Passat_b6_builder, Skoda_Fabia_builder):
        builder = it()
        director.set_builder(builder)
        director.make_auto()
        auto = builder.get_auto()
        print(auto)
        print(" ")

