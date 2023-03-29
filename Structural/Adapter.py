def roulette_in_inch(cls):                                       # При декорировании
    class Wrapper:
        def __init__(self, *args):                                # При создании экземпляро
            self.wrapped = cls(*args)
            setattr(self.wrapped, "length", getattr(self.wrapped, "length") * 39.37)
            setattr(self.wrapped, "units", "inch")

        def __getattr__(self, name):                             # При извлечении атрибутов
            return getattr(self.wrapped, name)
    return Wrapper


@roulette_in_inch
class Roulette():                                                 # Roulette = roulette_in_inch(Roulette)
    def __init__(self, x):                                        # Запускается методом Wrapper,__init__
        self.length = x
        self.units = 'metrs'

    def length_measurement(self):
        return f'довжина становить {self.length}  {self.units}'

d= Roulette(5)                                                   #В действительности вызывается Wrapper (5)
print(d.length_measurement())                                     #Запускается Wrapper. getattr