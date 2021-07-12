from Context import Context
from ConcreteStrategyA import ConcreteStrategyA
from ConcreteStrategyB import ConcreteStrategyB


print("Strategy pattern")
context = Context(ConcreteStrategyA())
print("StrategyDesign is set to normal sorting")
context.do_some_logic(["a","b","c","d","e"])
print()
print("StrategyDesign is set to reversed sorting")
context.strategy = ConcreteStrategyB()
context.do_some_logic(["a","b","c","d","e"])
