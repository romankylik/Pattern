from abc import ABC, abstractmethod


class Auto(ABC):
    """ Інтерфейс декоруємого обєкту"""
    @abstractmethod
    def cost(self) -> float:
        pass


class AutoBase(Auto):
    """Клас декоруємого обєкту"""
    def __init__(self, cost):
        self.__cost = cost

    def cost(self) -> float:
        return f'{self.__cost} $'


class Decorator(Auto):
    """Інтерфейс декоратора"""
    @abstractmethod
    def name(self) -> str:
        pass
    @abstractmethod
    def comfort(self) -> str:
        pass
    def __str__(self):
        return f"Авто {self.name()} {self.comfort()} та його вартість {self.cost()}"
class AutoSkoda(Decorator):
    """На основі базової комплектації AutoBase получаємо авто Skoda"""
    def __init__(self, wrapped: Auto, auto_cost: float): # auto_cost - при створені екземпляра класу, вказуємо скільки доплачуємо за comfort
        self.__wrapped = wrapped
        self.__cost = auto_cost
        self.__name = "Skoda"

    def cost(self) -> float:
        return f'{self.__cost +int(self.__wrapped.cost().split(" ")[0])} $'

    def name(self) -> str:
        return self.__name

    def comfort(self) -> str:
        return f'доукомплектовано кондиціонером'



class AutoWolksvagen(Decorator):
    """На основі базової комплектації AutoBase получаємо авто Skoda"""

    def __init__(self, wrapped: Auto,
                 auto_cost: float):  # auto_cost - при створені екземпляра класу, вказуємо скільки доплачуємо за comfort
        self.__wrapped = wrapped
        self.__cost = auto_cost
        self.__name = "Wolksvagen"

    def cost(self) -> float:
        return f'{self.__cost +int(self.__wrapped.cost().split(" ")[0])} $'

    def name(self) -> str:
        return self.__name

    def comfort(self) -> str:
        return f'доукомплектовано парктроніками'

# Клієнський код

if __name__ == "__main__":


    auto_base = AutoBase(5000)
    print(f"Вартість базової комплектації автомобіля = {auto_base.cost()}")
    skoda = AutoSkoda(auto_base, 2000)
    print(skoda)
    wolksvagen = AutoWolksvagen(auto_base, 3500)
    print(wolksvagen)

