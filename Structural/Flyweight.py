class Flyweight:
    """Клас легковеса, (стале значення для всіх обєктів, внутрішній стан)"""
    def __init__(self, shared_state):
        self.shared_state = shared_state   #спільний стан (зовнішній стан)

    def __str__(self):
        return str(self.shared_state)


class Person:
    """Персона.
    Незмінні дані об’єктів прийнято називати «внутрішнім станом». Всі інші дані — це «зовнішній стан»."""

    def __init__(self, unique_state, flyweight: Flyweight):
        self.unique_state = unique_state   #Унікальні параметри персони
        self.flyweight = flyweight   # Спільні параметри людей( легковес )

    def __str__(self):
        return f" Паспорт конкретної людини: {self.unique_state} \n" \
               f" Спільне місто: {self.flyweight}"


class FlyWeightFactory:

    _flyweights: dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights) -> None:

        for state, flyweight in initial_flyweights.items():
            self._flyweights[state] = Flyweight(flyweight)

    def get_flyweight(self, shared_st: dict) -> Flyweight:
        key = list(shared_st.keys())[0]
        if not self._flyweights.get(key):
            self._flyweights[key] = Flyweight(shared_st[key])
        return self._flyweights[key]

    @property
    def total(self):
        return len(self._flyweights)

    def list_flyweights(self) -> None:
        print(f"FlyweightFactory: Я маю {len(self._flyweights)} легковесов:")
        for key, value in self._flyweights.items():
            print(f"Стан: {key}, легковес: {value}")


class Creation_study_group:
    """Створення групи"""

    def __init__(self, flyweight_factory: FlyWeightFactory):
        self.flyweight_factory = flyweight_factory
        self.all_persons = []

    def make_person(self, unique_state, shared_state) -> Person:
        flyweight = self.flyweight_factory.get_flyweight(shared_state)
        person = Person(unique_state, flyweight)
        self.all_persons.append(person)

        return person


if __name__ == "__main__":
    flyweight_factory = FlyWeightFactory({"місто1": 'м.Київ'})
    group_maker = Creation_study_group(flyweight_factory)

    shared_states = [{"місто1": 'м.Київ'}, {"місто2": 'м.Одеса'},{ "місто3": 'м.Львів'}]                      #- спільне( внутрішній стан)
    unique_states = ['КС852', 'КУ932', 'ММ345', 'ВМ375', 'ЦМ445', 'ЬМ375', 'ЙЙ375', 'ЯХ375']   # унікальний параметр окремого обєкта ( серія та номер паспорта)

    group = [group_maker.make_person(x, shared_states[0])
              for x in unique_states[:2]]
    group.extend([group_maker.make_person(x, shared_states[1])
              for x in unique_states[2:5]])
    group.extend([group_maker.make_person(x, shared_states[2])
                  for x in unique_states[5:]])

    print(f"Створено групу для навчання з {len(group)} людей")
    print(f"У групі люди з {flyweight_factory.total} міст.")
    for index, person in enumerate(group):
        print("-"*20)
        print(person)

    flyweight_factory.list_flyweights()