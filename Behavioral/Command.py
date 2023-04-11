from abc import ABC, abstractmethod
from typing import List
from random import randrange


class Command(ABC):
    """Інтерфейс, для виконання операцій"""
    @abstractmethod
    def execute(self) -> None:
        ...



class Input_Operator:
    def accept_call(self):
        print("Оператор приймає виклик")

    def find_specialist(self):
        print("Оператор шукає спеціаліста відповідного напрямку")

    def switch_call(self):
        print("Переключає дзвінок на відповідного спеціаліста")


class Finances_Op:
    def fin_accept_call(self):
        print("Фінансовий спеціаліст приймає виклик")

    def fin_solove_problem(self):
        print("Фінансовий спеціаліст вирішує проблему")

    def fin_wish_good_day(self):
        print("Фінансовий спеціаліст бажає всього найкращого клієнту")


class Technical_Op:
    def tech_accept_call(self):
        print("Технічний спеціаліст приймає виклик")

    def tech_solove_problem(self):
        print("Технічний спеціаліст вирішує проблему")

    def tech_wish_good_day(self):
        print("Технічний спеціаліст бажає всього найкращого клієнту")


class AcceptCallCommand(Command):
    """Клас команди прийняти вхідний виклик"""
    def __init__(self, executor: Input_Operator):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.accept_call()


class FindSpecialistCommand(Command):
    """Клас команди, знайти спеціаліста який вирішить проблему клієнта"""
    def __init__(self, executor: Input_Operator):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.find_specialist()


class SwitchCallCommand(Command):
    """Клас комади для переключення дзвінка на потрібного спеціаліста"""
    def __init__(self, executor: Input_Operator):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.switch_call()


class FinancesAcceptCallCommand(Command):
    """Клас команди прийняти вхідний дзвінок фінансовому спеціалісту"""
    def __init__(self, executor: Finances_Op):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.fin_accept_call()


class FinancesSoloveProblemCommand(Command):
    """Клас команди вирішити проблему фінансовому спеціалісту"""
    def __init__(self, executor: Finances_Op):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.fin_solove_problem()


class FinancesWishGooDayCommand(Command):
    """Клас команди побажання від фінансового спеціаліста"""
    def __init__(self, executor: Finances_Op):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.fin_wish_good_day()

class TechnicalAcceptCallCommand(Command):
    """Клас команди прийняти вхідний дзвінок технічному спеціалісту"""
    def __init__(self, executor: Technical_Op):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.tech_accept_call()


class TechnicalSoloveProblemCommand(Command):
    """Клас команди вирішити проблему технічному спеціалісту"""
    def __init__(self, executor: Technical_Op):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.tech_solove_problem()


class TechnicalWishGooDayCommand(Command):
    """Клас команди побажання від технічного спеціаліста"""
    def __init__(self, executor: Technical_Op):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.tech_wish_good_day()

class CallCenter:
    """Клас агрегації всіх команд для операторів кол центру"""
    def __init__(self):
        self.history: List[Command] = []

    def addCommand(self, command: Command) -> None:
        self.history.append(command)

    def input_call(self) -> None:
        if not self.history:
            print("Немає вхідних дзвінків")
        else:
            for executor in self.history:
               executor.execute()

        self.history.clear()


if __name__ == "__main__":
    inp_operator = Input_Operator()
    finans_operator = Finances_Op()
    tech_operator = Technical_Op()
    call_centr = CallCenter()
    # При вхідному дзвінку до кол-центру, формуємо команди операторів
    call_centr.addCommand(AcceptCallCommand(inp_operator))
    call_centr.addCommand(FindSpecialistCommand(inp_operator))
    call_centr.addCommand(SwitchCallCommand(inp_operator))
    if randrange(0, 2): # Рандомно визначаємо чи проблема технічного чи фінансового характеру
        call_centr.addCommand(FinancesAcceptCallCommand(finans_operator))
        call_centr.addCommand(FinancesSoloveProblemCommand(finans_operator))
        call_centr.addCommand(FinancesWishGooDayCommand(finans_operator))
    else:
        call_centr.addCommand(TechnicalAcceptCallCommand(tech_operator))
        call_centr.addCommand(TechnicalSoloveProblemCommand(tech_operator))
        call_centr.addCommand(TechnicalWishGooDayCommand(tech_operator))
    # запускаємо процес вхідного дзвінка в колл-центр
    call_centr.input_call()
