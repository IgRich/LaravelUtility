from abc import ABCMeta, abstractmethod
from Commands.ConfigData import ConfigData


class BaseCommand:
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self, data: ConfigData) -> ConfigData:
        """Возвращает массив комманд"""
