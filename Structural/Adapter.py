def Roulette_in_inch(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)
            setattr(self.wrapped, "length", getattr(self.wrapped, "length") * 39.37)
            setattr(self.wrapped, "units", "inch")
        def __getattr__(self, name) :
            return getattr(self.wrapped, name)
    return Wrapper


@Roulette_in_inch
class Roulette():
    def __init__(self, x):
        self.length = x
        self.units = 'metrs'
    def length_measurement(self):
        return f'довжина становить {self.length}  {self.units}'

d= Roulette(18)
print(d.length_measurement())