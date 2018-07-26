from abc import ABCMeta, abstractmethod


class BaseCommand:
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self) -> list:
        """Запуск команды"""
