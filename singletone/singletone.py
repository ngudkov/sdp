#!/usr/bin/env python3

from random import choice
from string import ascii_lowercase

"""
Шаблон singleton.
Применим когда требуется внутри одного процесса иметь один и только один
экземпляр класса.

Типовая задача: получение токена авторизации.
Токен должен быть один всё время работы процесса.
"""


class SingletonMeta(type):
    """
    Родительский класс, реализующий логику одиночки
    """
    _instance = None

    def __call__(self):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Singleton(metaclass=SingletonMeta):

    """
    Класс наследник, выполняющий подключение и получение токена
    """

    auth_token = None

    def get_token(self, length):
        """
        Получение токена
        """

        if self.auth_token is None:
            self.auth_token = ''.join(choice(ascii_lowercase) for i in range(length))
        else:
            print('Вот тут мы пишем в лог, что пользователь нашего класса офигел и у него уже есть токен')


if __name__ == "__main__":

    s1 = Singleton()
    s1.get_token(20)
    s1.get_token(8888)

    s2 = Singleton()

    if id(s1.auth_token) == id(s2.auth_token):
        print("Оба объекта имеют одинаковый токен")
        print('Да и на самом деле у нас две ссылки на один и тот же объект')
        exit(0)
    print("Всё пропало, шеф!")
