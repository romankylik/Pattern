from abc import abstractmethod, ABC
class Flyweight:
    """Клас легковеса, (стале значення для всіх обєктів, внутрішній стан)"""
    def __init__(self, shared_state):
        self.shared_state = shared_state   #спільний стан

    def __str__(self):
        return str(self.shared_state)


class Person:
    """Персона.
    Незмінні дані об’єкта прийнято називати «внутрішнім станом». Всі інші дані — це «зовнішній стан»."""

    def __init__(self, unique_state, flyweight: Flyweight):
        self.unique_state = unique_state   #Унікальні параметри персони
        self.flyweight = flyweight   # Спільні параметри людей( легковес )

    def __str__(self):
        return f" Паспорт конкретної людини: {self.unique_state} \n" \
               f" Спільне місто: {self.flyweight}"


class FlyWeightFactory:

    def __init__(self):
        self.flyweights = []   #_Списоск легковесов

    def get_flyweight(self, shared_st) -> Flyweight:

        one_flyweights = list(filter(lambda x: x.shared_state == shared_st, self.flyweights))
        if one_flyweights:
            return one_flyweights[0]
        else:
            one_flyweight = Flyweight(shared_st)
            self.flyweights.append(one_flyweight)
            return one_flyweight

    @property
    def total(self):
        return len(self.flyweights)

class IOrder(ABC):
    @abstractmethod
    def make_person(self, unique_state, shared_state) -> Person:
        pass

class Creation_study_group(IOrder):
    """Створення групи"""

    def __init__(self, flyweight_factory: FlyWeightFactory):
        self.flyweight_factory = flyweight_factory
        self.all_persons = []

    def make_person(self, unique_state, shared_state) -> Person:
        flyweight = self.flyweight_factory.get_flyweight(shared_state)
        person = Person(unique_state, flyweight)
        self.all_persons.append(person)
        return person


class Proxy_study_group(IOrder):
    """///"""

    def __init__(self, real_subject: Creation_study_group):
        self.__real_subject = real_subject
    def make_person(self, unique_state, shared_state) -> Person:
        self.__logging(unique_state, shared_state)
        return self.__real_subject.make_person(unique_state, shared_state)

    def check_access(self) -> bool:
        print('Перевірка проксі')
        return self.__real_subject is not None

    def __logging(self, unique_state, shared_state) -> None:
        print(f"====Логуємі дані людини (додаткова логіка...)====\n"
              f" Паспорт конкретної людини: {unique_state} \n" 
               f" Спільне місто: {shared_state}")


if __name__ == "__main__":
    flyweight_factory = FlyWeightFactory()
    group_maker = Creation_study_group(flyweight_factory)
    log_proxy = Proxy_study_group(group_maker)

    shared_states = ['м.Київ', 'м.Одеса', 'м.Львів']                           #- спільне( внутрішній стан)
    unique_states = ['КС852', 'КУ932', 'ММ345', 'ВМ375', 'ЦМ445', 'ЬМ375', 'ЙЙ375', 'ЯХ375']   # унікальний параметр окремого обєкта ( серія та номер паспорта)

    group = [log_proxy.make_person(x, shared_states[0])
              for x in unique_states[:2]]
    group.extend([log_proxy.make_person(x, shared_states[1])
              for x in unique_states[2:5]])
    group.extend([log_proxy.make_person(x, shared_states[2])
                  for x in unique_states[5:]])

    print(f"--------------------------\n"
        f"Створено групу для навчання з {len(group)} людей")
    print(f"У групі люди з {flyweight_factory.total} міст.")
