from abc import ABC, abstractmethod


class ABCIngredients(ABC):
    """Інтерфейс інгридієнтів"""
    @abstractmethod
    def cost(self) -> float:
        pass
    @abstractmethod
    def name(self) -> str:
        pass


class Product(ABCIngredients):
    """Клас інгридієнта"""
    def __init__(self, name: str, cost: float):
        self.__cost = cost
        self.__name = name

    def cost(self) -> float:
        return self.__cost

    def name(self) -> str:
        return self.__name


class CompoundProduct(ABCIngredients):
    """Клас компонуємих інгридієнтів"""
    def __init__(self, name: str):
        self.__name = name
        self.products = []

    def cost(self):
        cost = 0
        for it in self.products:
            cost += it.cost()
        return cost

    def name(self) -> str:
        return self.__name

    def add_product(self, product: ABCIngredients):
        self.products.append(product)

    def remove_product(self, product: ABCIngredients):
        self.products.remove(product)

    def clear(self):
        self.products = []


class Hamburger(CompoundProduct):
    """Клас гамбургера"""
    def __init__(self, name: str):
        super(Hamburger, self).__init__(name)

    def cost(self):
        cost = 0
        for it in self.products:
            cost_it = it.cost()
            print(f"Вартість '{it.name()}' = {cost_it} гривень")
            cost += cost_it
        print(f"Вартість гамбургера '{self.name()}' = {cost} гривень")
        return cost


if __name__ == "__main__":
    dough = CompoundProduct("тісто")
    dough.add_product(Product("мука", 3))
    dough.add_product(Product("яйце", 2.3))
    dough.add_product(Product("сіль", 1))
    dough.add_product(Product("цукор", 2.1))
    sauce = Product("Барбекю", 12.1)
    topping = CompoundProduct("топпинг")
    topping.add_product(Product("Дор блю", 14))
    topping.add_product(Product("Пармезан", 12.3))
    topping.add_product(Product("Моцарелла", 9.54))
    topping.add_product(Product("Маасдам", 7.27))
    pizza = Hamburger("4 сира")
    pizza.add_product(dough)
    pizza.add_product(sauce)
    pizza.add_product(topping)
    print(pizza.cost())
