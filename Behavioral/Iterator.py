from typing import List
from collections.abc import Iterable, Iterator


class PersonItem:
    """Об'єк з яких складатиметься колекція"""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Персона з ім'ям: {self.name}"


class My_Iterator(Iterator):
    """Сам ітератор, з можливістю ітерувати
                в порядку зростання або ж в алфавітному порядку"""
    def __init__(self, person: List[PersonItem],
                 alphabetical_iter: bool = False):
        self._person = person
        self._index: int = 0
        self._alphabetical_iter = alphabetical_iter
        self.alphabetical_sort_list = sorted(self._person, key=lambda x: x.name) # Відсортований список в алфавітному порядку

    def __next__(self) -> PersonItem:
        try:
            if self._alphabetical_iter:
                person_item = self.alphabetical_sort_list [self._index]
                self._index += 1
            else:
                person_item = self._person[self._index]
                self._index += 1
        except IndexError:
            raise StopIteration()
        return person_item


class Group(Iterable):
    """Група людей наповнена обєктами PersonItem"""
    def __init__(self, amount_person: List):
        self._slices = [PersonItem(it) for it in amount_person]
        print(f" Створена група з {len(amount_person)} людей")

    def amount_person(self) -> int:
        return len(self._slices)

    def __iter__(self) -> My_Iterator:
        return My_Iterator(self._slices)

    def get_alphabetical_iterator(self) -> My_Iterator:
        return My_Iterator(self._slices, True)


if __name__ == "__main__":
    group_one = Group(["Vasua", "Ihor", "Petro", "Max", "Nazar", "Andriy"])
    print("*  " + "Відсортуємо в порядку додавання в групу" + "  *")
    for ind, item in enumerate(group_one):
        print(str(ind+1) + ". " + str(item))

    print("*  " + "Відсортуємо тепер в алфавітному порядку" + "  *")
    iterator = group_one.get_alphabetical_iterator()
    for ind, item in enumerate(iterator):
        print(str(ind+1) + ". " + str(item))