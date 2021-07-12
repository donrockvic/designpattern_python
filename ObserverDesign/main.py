from Subject import Subject
from Observer import Observer

from ConcreteSubject import ConcreateSubject
from ConcreteObserverA import ConcreteObserverA
from ConcreteObserverB import ConcreteObserverB


if __name__ == "__main__":
    subject = ConcreateSubject()
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic(3)
    subject.some_business_logic(0)

    subject.detach(observer_b)

    subject.some_business_logic(5)




