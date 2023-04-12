from abc import ABC, abstractmethod
from typing import List


class Auto:
    """Клас виготовляємого автомобіля"""
    def __init__(self):
        self.__state: List[str] = ['base']

    def add_element(self, element: str) -> None:
        print(f"В атомобіль добавлено: {element}")
        self.__state.append(element)

    def __str__(self):
        return f"Автомобіль складається з: {self.__state}"


class AutoPickingDepartment(ABC):
    """Базовий клас шаблоного метода збирання автомобіля"""
    def make_auto(self, auto: Auto) -> None:
        self.set_body(auto) # Задати каркас
        self.set_comfort(auto)  # Задати колеса
        self.paint_auto(auto)  # Пофарбувати автомобіль

    @abstractmethod
    def set_body(self, auto: Auto) -> None:
        ...

    @abstractmethod
    def set_comfort(self, auto: Auto) -> None:
        ...

    @abstractmethod
    def paint_auto(self, auto: Auto) -> None:
        ...


class SedanAuto(AutoPickingDepartment):
    """Клас виготовлення автомобіля седан"""

    def set_body(self, auto: Auto) -> None:
        auto.add_element("Каркас форми седан")
        auto.add_element("4 дверки")
        auto.add_element("Колеса")
        auto.add_element("Електричний двигун")

    def set_comfort(self, auto: Auto) -> None:
        auto.add_element("Магнітолу")
        auto.add_element("Кондиціонер")


    def paint_auto(self, auto: Auto) -> None:
        auto.add_element("Пофарбована в зелений")
        print("Автомобіль готовий до використання")


class SmartAuto(AutoPickingDepartment):
    """Клас виготовлення автомобіля смарт"""

    def set_body(self, auto: Auto) -> None:
        auto.add_element("Каркас форми смарт")
        auto.add_element("2 дверки")
        auto.add_element("Колеса")
        auto.add_element("Дизельний двигун")

    def set_comfort(self, auto: Auto) -> None:
        auto.add_element("Дуйка")
        auto.add_element("Підігрів руля")
        auto.add_element("Парктроніки")

    def paint_auto(self, auto: Auto) -> None:
        auto.add_element("Пофарбована в червоний")
        print("Автомобіль готовий до використання")


class Factory:
    """Клас заводу по виготовленю автомобілів"""
    def __init__(self, template_auto: AutoPickingDepartment):
        self.__collect = template_auto

    def set_output_template(self, template_auto: AutoPickingDepartment):
        self.__collect = template_auto

    def make_auto(self) -> Auto:
        auto = Auto()
        self.__collect.make_auto(auto)
        return auto


if __name__ == "__main__":
    factory = Factory(SmartAuto())
    print("*"*8 + "Збираємо автомобіль Седан"+8*"*")
    print(factory.make_auto())
    print("-" * 8 + "Збираємо автомобіль Смарт" + 8 * "-")
    factory.set_output_template(SedanAuto())
    print(factory.make_auto())