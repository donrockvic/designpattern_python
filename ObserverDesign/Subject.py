from abc import ABC, abstractmethod

from Observer import Observer

class Subject(ABC):
    """
    The subject interface declare a set of methos for mapping subscriber
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach oberver to the subject
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an oberver from the subject
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify akk iberver about an event
        """
        pass
