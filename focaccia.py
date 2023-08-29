import math
def pluralize(singular,  plural,  number):
    if number == 1:
        return singular
    else:
        return plural

def TotalCost(totalCostFlour, totalCostYeast, totalCostSalt, totalCostOil):
    COST_FLOUR = 2.69
    COST_YEAST = 0.4
    COST_SALT = 0.49
    COST_OIL = 6.39
    totalCostFlour *= COST_FLOUR
    totalCostYeast *= COST_YEAST
    totalCostSalt *= COST_SALT
    totalCostOil *= COST_OIL
    return totalCostFlour + totalCostYeast + totalCostSalt + totalCostOil


print('How many people do you need to serve?', end=' ')
people = input()
people = float(people)
print()
print()

PEOPLE_PER_FOCACCIA = 4
loavesFoccacia = 0
loavesFoccacia = people / PEOPLE_PER_FOCACCIA
loavesFoccacia = math.ceil(loavesFoccacia)

print('You need to make', end=' ')
print(loavesFoccacia, end=' ')
print(pluralize('loaf', 'loaves', loavesFoccacia), end=' ')
print('of foccacia')
print()
print('Shopping List for Focaccia Bread')
print('--------------------------------')

FLOUR_CUPS_PER_LOAF = 5
FLOUR_CUPS_PER_BAG = 20

flourBags = (loavesFoccacia * FLOUR_CUPS_PER_LOAF) / FLOUR_CUPS_PER_BAG
flourBags = math.ceil(flourBags)

print(flourBags, end=' ')
print(pluralize('bag', 'bags', flourBags), end= ' of flour')
print()

TSP_YEAST_PER_LOAF = 1.75
TSP_YEAST_PER_PACKAGE = 2.25

packagesYeast = (loavesFoccacia * TSP_YEAST_PER_LOAF) / TSP_YEAST_PER_PACKAGE
packagesYeast = math.ceil(packagesYeast)

print(packagesYeast, end= ' ')
print(pluralize('package', 'packages', packagesYeast), end= ' of yeast')
print()

TSP_SALT_PER_LOAF = 1.875
GRAMS_SALT_PER_TSP = 5
GRAMS_SALT_PER_CONTAINER = 30

canistersSalt = (loavesFoccacia * TSP_SALT_PER_LOAF * GRAMS_SALT_PER_TSP) / GRAMS_SALT_PER_CONTAINER
canistersSalt = math.ceil(canistersSalt)

print(canistersSalt, end=' ')
print(pluralize('canister', 'canisters', canistersSalt), end=' of salt')
print()

TBSP_OLIVE_OIL_PER_LOAF = 2
ML_PER_TBSP = 14.8
ML_PER_BOTTLE_OLIVE_OIL = 500.0

bottlesOliveOil = (loavesFoccacia * TBSP_OLIVE_OIL_PER_LOAF * ML_PER_TBSP) / ML_PER_BOTTLE_OLIVE_OIL
bottlesOliveOil = math.ceil(bottlesOliveOil)

print(bottlesOliveOil, end= ' ')
print(pluralize('bottle', 'bottles', bottlesOliveOil), end= ' of olive oil')
print()
print('Total expected cost of ingredients: $ ', end= str(TotalCost(flourBags, packagesYeast, canistersSalt, bottlesOliveOil)))
print() 
print('Have a great party!')