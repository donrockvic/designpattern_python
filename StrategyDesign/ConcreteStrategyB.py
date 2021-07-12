from typing import List

from Strategy import Strategy


class ConcreteStrategyB(Strategy):
    @classmethod
    def do_algorithm(cls, data: List) -> List:
        return reversed(sorted(data))
