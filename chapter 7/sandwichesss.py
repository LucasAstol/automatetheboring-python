import pyinputplus as pyip

BREADS = {'wheat': 1, 'white': 2, 'sourdough': 4}
PROTEINS = {'chicken': 4, 'turkey':4.5, 'ham': 3, 'tofu': 3.5}
CHEESES = {'cheddar': 3, 'Swiss':3.4, 'mozzarella':2}
TOPPINGS = {'mayo':1, 'mustard':1, 'lettuce':0.5, 'tomato':0.7}

price = 0

breadType = pyip.inputMenu(choices=list(BREADS.keys()), default='wheat')
price += BREADS.get(breadType)

proteinType = pyip.inputMenu(choices=list(PROTEINS.keys()), default='chicken')
price += PROTEINS.get(proteinType)

if('yes' == pyip.inputYesNo('Do you want cheese?')):
    cheese = pyip.inputMenu(choices=list(CHEESES.keys()),default='mozzarella')
    price += CHEESES.get(cheese)

if('yes' == pyip.inputYesNo('Do you want toppings?')):
    topping = pyip.inputMenu(choices=list(TOPPINGS.keys()),default='mayo')
    price += TOPPINGS.get(topping)

numSand = pyip.inputInt('How many sandwiches would you like?', min=1)


print('Total price is: %s' % (price * numSand))