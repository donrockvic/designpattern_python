from typing import List
from random import randrange

from Subject import Subject
from Observer import Observer


class ConcreateSubject(Subject):
    """
    The Subject owns some important state and notifies oberver when the state changes
    """

    _state: int =  None 
    _observers : List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attahed an Observer")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        """
        Trigger when the state change and notig all the Observer
        """
        print("Notifying Observers....")
        for observer in self._observers:
            observer.update(self._state)
    
    def some_business_logic(self, data) -> None:
        """
        Some business logic
        """
        print("\nSubject: Something changes")
        self._state = data

        print(f"Subject: My state has cahnge to: {self._state}")
        self.notify()
        


