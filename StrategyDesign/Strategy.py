from typing import List
from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    The interface for all realted strategey used by context class dynamically
    """

    @abstractmethod
    def do_algorithm(self, data: List):
            pass