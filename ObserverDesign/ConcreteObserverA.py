from Observer import Observer


class ConcreteObserverA(Observer):
    def update(self, data: int) -> None:
        if data < 3:
            print("ConcreteObserverA: Reacted and event")
