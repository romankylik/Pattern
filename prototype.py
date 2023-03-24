from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self): pass

class StudentsGroup(Prototype):
    """Мій приклад це прототип робочого класу(групи) в школі або інституті"""
    def __init__(self, name_group, tutor, students: []):
        self.name_group = name_group
        self.tutor = tutor
        self.students = students

    def __str__(self):
        return f'Вітаємо {self.students}, це група {self.name_group}, вашим викладачем буде {self.tutor}'

    def clone(self):
        students = list(i for i in self.students)
        return type(self)(self.name_group, self.tutor, students)


group = StudentsGroup('Learning English', 'Василь Петрович', ['students1', 'students2'])
print(group)


new_group = group.clone()
new_group.name_group, new_group.tutor = "Math", "Олег Богданович"
new_group.students.append("учень3") # Або ж new_group.students = ["учень3", "учень4", "учень5"]

print(group)
print(new_group)