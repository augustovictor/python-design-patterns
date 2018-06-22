from strategy import StrategyFedex
from strategy import StrategyUps
from strategy.Context import Context
from observer.Subject import Subject
from observer.AbsSubject import AbsSubject
from observer.Observer import Observer

# Subject
subject = Subject()
subject.publish('Value woohooo')

# Observers
o1 = Observer()
o2 = Observer()

subject.add_observer(o1)
subject.add_observer(o2)

# StrategyFedex
strategy = StrategyFedex.StrategyFedex(10)
total = Context(strategy).calculate_total()

subject.publish(f'Total value with StrategyFedex: {total}')

o1.post_something('Post from observer')

# StrategyUps
strategy = StrategyUps.StrategyUps(10)
total = Context(strategy).calculate_total()

subject.publish(f'Total value with StrategyFedex: {total}')
print('all good')