def singleton(cls):
    _instances = {}
    def get_instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return get_instance

@singleton
class Notebook:
    """Цей приклад паттерна я представив у вигляді записника(органайзера). Коли ти записуєш якісь нагадування або нотатки
    то записуєш в один і той же записник, а не купляєш новий.
    Також ти повинен мати доступ до записника завжди під рукою( глобальна точка доступу)"""

    def set_note(self, text):
        print(f'Записали нотатку {text}')
        """записуємо нотатку в текстовий файл"""



a = Notebook()
b = Notebook()
print(a) # Output: 1
print(b) # Output: 1
print(a == b)
#a.set_note("1234")
Notebook