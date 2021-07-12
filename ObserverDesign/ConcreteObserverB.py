from Observer import Observer


class ConcreteObserverB(Observer):
    def update(self, data: int) -> None:
        if data ==0 or data >= 2:
            print("ConcreteObserverB: Reacted and event")
