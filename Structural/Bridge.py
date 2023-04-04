from abc import *

class Engine(ABC):
    """Інтерфейс двигуна ( Перша ієрархія класів)"""
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def spin_the_wheels(self):   #крутити колеса
        pass


class ConcretEngine(Engine):
    """Реалізація інтерфейсу Engine ( Друга ієрархія класів)"""
    def start_engine(self):
        return "is started"
    def spin_the_wheels(self):
        return "is going"



class Auto(ABC):
    """Інтерфейс автомобіля ( Друга ієрархія класів)"""


    def __init__(self, name: str, engine: Engine):
        self.name = name
        self.engine = engine
        self._status = "not started"
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def start_car(self):
        pass


class Skoda(Auto):
    """Реалізація інтерфейсу Auto ( Друга ієрархія класів)"""
    def start_car(self):
        if self._status == "not started":
            a = self.engine.start_engine()
            self._status = a
            return f"Автомобіль {self.name} {self._status}."
        else:
            return f"Автомобіль {self.name} уже заведений."

    def drive(self):
        if self._status == "is started":
            return f"Автомобіль {self.name} {self.engine.spin_the_wheels()}"
        else:
            print("Спочатку заведемо авто, тоді поїдемо")
            self.start_car()
            return self.drive()


if __name__ == '__main__':

    new_engine = ConcretEngine("Benzine")
    new_auto = Skoda("Skoda", new_engine)

    print(new_auto.start_car())
    print(new_auto.drive())
