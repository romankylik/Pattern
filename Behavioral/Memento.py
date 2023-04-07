from typing import List


class Memento:
    """Клас Знімок, фіксує поточний стан обєкта"""
    def __init__(self, state: List[str]):
        self.__state = state

    def get_state(self) -> List[str]:
        return self.__state[:]


class Collage_Foto:
    """Клас колаж з базовою фотографією"""
    def __init__(self):
        self.__state: List[str] = ["Фон"]

    def add_foto(self, foto: str) -> None:
        print(f"В колаж добавлено фото: {foto}")
        self.__state.append(foto)

    def create_memento(self):
        return Memento(self.__state[:])

    def set_memento(self, memento: Memento):
        self.__state = memento.get_state()

    def __str__(self):
        return f"Поточний стан колажу: {self.__state}"


class Graphic_Editor:
    """Графічний редактор, який редагує колаж"""
    def __init__(self, collage: Collage_Foto):
        self.collage = collage
        self.collage_states: List[Memento] = []

    def add_foto_to_collage(self, foto: str):
        self.collage_states.append(self.collage.create_memento())
        self.collage.add_foto(foto)


    def cancel_add_foto(self):
        if len(self.collage_states) == 1:
            self.collage.set_memento(self.collage_states[0])
            print("Колаж повернувся в свій початковий стан")
            print(self.collage)
        else:
            print("Скасовано попередню дію")
            state = self.collage_states.pop()
            self.collage.set_memento(state)
            print(self.collage)


if __name__ == "__main__":
    new_collage = Collage_Foto()
    editor = Graphic_Editor(new_collage)
    print(new_collage)
    print("*  " + "Добавляємо фотографії в колаж" + "  *")
    editor.add_foto_to_collage('фото дітей')
    editor.add_foto_to_collage('фото жінки')
    editor.add_foto_to_collage('фото батьків')
    print(new_collage)
    print("////" + "Скасовуємо попередні дії" + "////")
    editor.cancel_add_foto()
    editor.cancel_add_foto()
    editor.cancel_add_foto()
    print("-----" + "Добавляємо інші (нові) фото" + "-----")
    editor.add_foto_to_collage('весільні фото')
    editor.add_foto_to_collage('відпустка')
    print(new_collage)