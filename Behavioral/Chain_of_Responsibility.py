from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional, TypeVar

T = TypeVar("T")


class Call(Enum):
    """Тип запиту"""
    PIN_COD = 1
    FINANCES= 2
    TARIFF = 3
    NOT_ORDER = 4


class Request:
    """Клас запиту на обслуговування від клієнта"""

    def __init__(self, problem: str, order_type: Call):
        self.__problem = problem  #_Опис проблеми
        self.__order_type = order_type  #_Тип проблеми( змінити пінкод, змінити тарифний план, пропали гроші і тд...)

    @property
    def call_type(self):
        return self.__order_type

    @property
    def problem(self):
        return self.__problem


class Handler(ABC):
    """Базовий клас по обробці запитів. ( Умовно базовий клас операторів)"""

    def __init__(self, successor: Optional[T] = None):
        self.__successor = successor   # наступний, хто має обробляти запит

    def handle(self, request: Request) -> None:
        res = self._check_request(request.call_type)
        if not res and self.__successor:
            for i in self.__successor:
                if i.direction == request.call_type:
                    i.handle(request)

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, successor: Optional[T]):
        self.__successor = successor

    @abstractmethod
    def _check_request(self, request_type: Call) -> bool:
        ...


class Input_Operator(Handler):
    """Клас обробки запиту оператором вхідних дзвінків"""

    def __init__(self, successor: Handler = None):
        super().__init__(successor)

    def _check_request(self, request_type: Call) -> bool:
        check = request_type in (Call.PIN_COD,
                                 Call.FINANCES,
                                 Call.TARIFF)
        if check:
            print("Оператор отримав дзвінок та переключає на відповідного спеціаліста")
        else:
            print("Оператор вирішив питання самостійно")
        return not check



class Finances_Operator(Handler):
    """Клас обробки запиту спеціалісту по оборобу коштів та тарифних планах"""

    def __init__(self, successor: Handler = None):
        super().__init__(successor)
        self.direction = Call.FINANCES

    def _check_request(self, request_type: Call) -> bool:
        check = request_type == self.direction
        if check:
            print("Фінансовий спеціаліст вирішив проблему запиту")
            print("_" * 5)
        else:
            print("Фінансовий спеціаліст не може допомогти")
        return not check

class TARIFF_Operator(Handler):
    """Клас обробки запиту спеціалісту по заміні пінкоду"""

    def __init__(self, successor: Handler = None):
        super().__init__(successor)
        self.direction = Call.TARIFF

    def _check_request(self, request_type: Call) -> bool:
        check = request_type == self.direction

        if check:
            print("Спеціаліст змінив тарифний план клієнту")
            print("_" * 5)
        else:
            print("Не вдалось змінити тарифний план")
        return not check

class Pin_Operator(Handler):
    """Клас обробки запиту спеціалісту по заміні пінкоду"""

    def __init__(self, successor: Handler = None):
        super().__init__(successor)
        self.direction = Call.PIN_COD

    def _check_request(self, request_type: Call) -> bool:
        check = request_type == self.direction

        if check:
            print("Технічний спеціаліст вирішив проблему по заміні пінкоду")
            print("_" * 5)
        else:
            print("Технічний спеціаліст не може допомогти")
        return not check



if __name__ == "__main__":
    finances = Finances_Operator()
    tech_op = Pin_Operator()
    tariff = TARIFF_Operator()
    input_call = Input_Operator([finances, tech_op, tariff])  # Завжди перший приймає дзвінок

    request_1 = Request("Було 180грн, і кудись пропали 100грн", Call.FINANCES) #поступив дзвінок, що пропали кошти з рахунку
    request_2 = Request("Прохання змінити тарифний план", Call.TARIFF)
    request_3 = Request("Забув пін код, допоможіть відновити", Call.PIN_COD)
    for i in [request_1, request_2, request_3]:
        input_call.handle(i)

