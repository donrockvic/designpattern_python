from Strategy import Strategy
from typing import  List

class Context():
    """
    The context defines the interface of interest to clients
    """
    def __init__(self, strategy: Strategy):
        """
        Constructor function to add strategy dynamically
        :param strategy:
        """
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The contect maintain a reference to the StrategyDesign object
        :return:
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Setter for strategy
        :param strategy:
        """
        self._strategy = strategy

    def do_some_logic(self, data: List) -> None:
        """
        work function
        """
        print("Content: sorting data using the strategy (not sure how it'll do it) ")
        result = self._strategy.do_algorithm(data)
        print("".join(result))
