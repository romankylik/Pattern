from random import randrange

class Color:
    def __init__(self):
        self. red = 'red'
        self.black = 'black'
        self.pink = "pink"

class Auto:
    def __init__(self, name):
        self.name = name
        self.color = [Color().red, Color().black, Color().pink][randrange(3)]



if __name__ == '__main__':
    new_auto = Auto("Skoda")
    new_auto2 = Auto("Renault")
    print(f"Створено новий автомобіль  {new_auto.name} кольору {new_auto.color}")
    print(f"Створено новий автомобіль  {new_auto2.name} кольору {new_auto2.color}")