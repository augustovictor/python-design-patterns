from strategy import StrategyFedex
from strategy import StrategyUps
from strategy import Context

# StrategyFedex
strategy = StrategyFedex.StrategyFedex(10)
total = Context.Context(strategy).calculate_total()
print(total)

# StrategyUps
strategy = StrategyUps.StrategyUps(10)
total = Context.Context(strategy).calculate_total()
print(total)

print('all good')