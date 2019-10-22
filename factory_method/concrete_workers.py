#!/usr/bin/env python3

from __future__ import annotations

from abstract_workers import WorkerCreator, Job


class DocManCreator(WorkerCreator):
    """
    Класс инициализации работника
    Работник документалист. Хочет производить документы, но только собирает их
    """

    def factory_method(self) -> DocMan1:
        return DocMan1()


class ManagerCreator(WorkerCreator):
    """
    Класс инициализации работника
    Управляющий. Хочет управлять, но ничем не управляет.
    Думает что выбирает кто какой документ будет делать,
    но на самом деле даже это делает не он.
    """

    def factory_method(self) -> Manager1:
        return Manager1()


class DocMan1(Job):
    def create_documentation(self) -> str:
        return 'Документалист весь день сидел на совещании и ничего не делал.'


class Manager1(Job):
    def create_documentation(self) -> str:
        return 'РП весь день сидел на совещании и ничего не делал.'

