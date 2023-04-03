
"""Різні типи меню .  Сворення інтерфейсу меню упущено"""
class VeganMenu():
    def get_name(self):
        return "Вегетаріанське меню"


class NotVeganMenu():
    def get_name(self):
        return "Не вегетаріанське меню"


class MixedMenu():
    def get_name(self):
        return "Змішане меню"


class Kitchen:
    """
    Кухня
    """
    def prepare_food(self):
        print("Замовлення готується!")

    def call_waiter(self):
        print("Кухня віддає замовлену їду офіціанту")

class Client():
    """
    Клас клієнта піцерії
    """
    def __init__(self, name: str):
        self.name = name

    def request_menu(self, menu):
        print(f"Клієнт {self.name} ознайомлюється з '{menu.get_name()}'")

    def form_order(self) -> dict:
        print(f"Клієнт {self.name} робить замовлення")
        return {}

    def eating_food(self):
        print(f"Клієнт {self.name} починає їсти")
        print("__________________________")

    def get_name(self):
        return self.name


class Waiter:
    """
    Офіціант
    """
    def take_order(self, client: Client):
        print(f"Оіціант прийняв замовлення від клієнта {client.get_name()}")

    def send_to_kitchen(self, kitchen: Kitchen):
        print("Офіціант відніс замовлення на кухню")

    def serve_client(self, client: Client):
        print(f"Готове замовлення офіціант відносить до клієнта {client.get_name()}!")


class RestaurantFacade:
    """
    Ресторан на основі паттерна Фасад
    """
    def __init__(self):
        self.kitchen = Kitchen()
        self.waiter = Waiter()
        self.menu = {"V": VeganMenu,
                     "N_V": NotVeganMenu,
                     "M": MixedMenu}

    def get_menu(self, type_menu):
        return self.menu[type_menu]()

    def take_order(self, client):
        self.waiter.take_order(client)
        self.waiter.send_to_kitchen(self.kitchen)
        self.__kitchen_work()
        self.waiter.serve_client(client)

    def __kitchen_work(self):
        self.kitchen.prepare_food()
        self.kitchen.call_waiter()




if __name__ == "__main__":
    restauran = RestaurantFacade()
    client1 = Client("Іван")
    client2 = Client("Василь")
    client1.request_menu(restauran.get_menu("M"))
    restauran.take_order(client1)
    client1.eating_food()
    client2.request_menu(restauran.get_menu("V"))
    restauran.take_order(client2)
    client2.eating_food()