from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Observer abstract class
    """

    @abstractmethod
    def update(self, data:int) -> None:
        """
        Recieve update from the Subject
        """
        pass