class Mediator:
    """Посередник """
    def __init__(self):
        self.customers = []
        self.products = []
        self.shopping_cart = ShoppingCart(self)
        self.orders = []
        self.payment = Payment(self)

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_product(self, product):
        self.products.append(product)

    def add_order(self, order):
        self.orders.append(order)

    def calculate_total_cost(self, customer):
        total_cost = 0
        for item in self.shopping_cart.product:
            total_cost += item.price
        return total_cost

    def check_product_availability(self, product):
        if product in self.products:
            return True
        else:
            return False

    def place_order(self, customer):
        if customer in self.customers:
            self.orders.append(Order(self.shopping_cart.product, self.calculate_total_cost(customer), customer))
            self.shopping_cart.clear()
        else:
            print("Покупця не знайдено")

    def make_payment(self, customer):
        if customer in self.customers:
            order = self.orders[-1]
            self.payment.process_payment(order, customer)
        else:
            print("Покупця не знайдено")


class Customer:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        self.mediator.add_customer(self)

    def add_to_cart(self, product: list):
        for prod in product:
            if self.mediator.check_product_availability(prod):
                self.mediator.shopping_cart.add_product(prod)
            else:
                print("Продукт недоступний")

    def place_order(self):
        self.mediator.place_order(self)

    def make_payment(self):
        self.mediator.make_payment(self)
    def __str__(self):
        return self.name

class Product:
    def __init__(self, name, price, mediator):
        self.name = name
        self.price = price
        self.mediator = mediator
        self.mediator.add_product(self)
    def __str__(self):
        return self.name


class ShoppingCart:
    """Клас корзини магазину """
    def __init__(self, mediator):
        self.mediator = mediator
        self.product = []

    def add_product(self, item):
        self.product.append(item)

    def clear(self):
        self.product = []


class Order:
    def __init__(self, items, total_cost, customer):
        self.product = items
        self.total_cost = total_cost
        self.customer = customer


class Payment:
    def __init__(self, mediator):
        self.mediator = mediator

    def process_payment(self, order, customer):
        print("Обробка платежу клієнта:", customer)
        print("Деталі замовлення:", *[str(i)+", " for i in order.product], "Загальна вартість:", order.total_cost, "грн.")


mediator = Mediator()

customer1 = Customer("Vasya", mediator)
customer2 = Customer("Maxim", mediator)

product1 = Product("Футболка", 20, mediator)
product2 = Product("Джинси", 50, mediator)

customer1.add_to_cart([product1, product2])

customer1.place_order()
customer1.make_payment()

product3 = Product("Кросівки", 42, mediator)
customer2.add_to_cart([product3,])
customer2.place_order()
customer2.make_payment()