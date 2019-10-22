#!/usr/bin/env python3

from __future__ import annotations
from abc import ABC, abstractmethod


class WorkerCreator(ABC):
    """
    Абстракный класс описывающий сотрудника и реализующий фабричный метод
    """

    @abstractmethod
    def factory_method(self) -> None:
        """
        Фабричный метод по умолчанию
        """
        pass

    def work(self) -> str:
        """
        Сотрудник производит документацию
        """

        obj = self.factory_method()

        # Далее, работаем с этим продуктом.
        result = f'Создано ещё немного документации и вот результат: {obj.create_documentation()}'

        return result


class Job(ABC):
    """
    Интерфейс Продукта объявляет операции, которые должны выполнять все
    конкретные продукты.
    """

    @abstractmethod
    def create_documentation(self) -> str:
        pass


