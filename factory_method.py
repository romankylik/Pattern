from abc import *

"""Інтерфейс для виготовлення продукту"""
class Product:
    def __init__(self):
        self.type = ""
    @abstractmethod
    def get_type(self) -> str:
        return self.type

"""Конкретний продукт"""
class  PlaneProduct(Product):
    def __init__(self):
        self.type = "Plane"
    def get_type(self) -> str:
        return self.type

class  TankProduct(Product):
    def __init__(self):
        self.type_pr = "Tank"
    def get_type(self) -> str:
        return self.type_pr
class  ArtilleryProduct(Product):
    def __init__(self):
        self.type = "Artillery"
    def get_type(self) -> str:
        return self.type

"""Клас творець."""
class FactoryProduct():
    def create_product(self, product_type: Product) -> Product:
        """
        Factory Method
        """
        factory_dict = {
            "Plane": PlaneProduct,
            "Tank": TankProduct,
            "Artillery": ArtilleryProduct
        }
        return factory_dict[product_type]()


if __name__ == '__main__':
    factory = FactoryProduct()
    my_product = factory.create_product("Tank")
    print(f'Виготовлено продукт {my_product.get_type()}')
