from typing import List

from Strategy import  Strategy


class ConcreteStrategyA(Strategy):
    @classmethod
    def do_algorithm(cls, data: List) -> List:
        return sorted(data)
