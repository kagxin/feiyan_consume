from db import m
import abc
from typing import Dict


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class ConsumerBase(abc.ABC, Singleton):
    """
        数据库连接，日志logger，放在这里
    """
    m = m

    @abc.abstractmethod
    def check(self, data: Dict) -> bool:
        pass

    @abc.abstractmethod
    def execute(self, data: Dict):
        pass
