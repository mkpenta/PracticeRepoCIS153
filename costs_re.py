import re

f = open('cost.txt', 'r')

pattern ='(.+) - (.+) \$([0-9]+\.[0-9][0-9])'

costs = {}

for line in f:
    line = line.rstrip()
    match = re.findall(pattern, line)
    t = match[0]
    mealName = t[0]
    mealDescription = t[1]
    mealCost = float(t[2])
   
    mealName = mealName.upper()
    
    if mealName not in costs:
        costs[mealName] = [mealCost]
    else:
        currentList = costs[mealName]
        currentList.append(mealCost)
        costs[mealName] = currentList
    
print(costs)
highestMeal = 0
highestCost = 0

for key in costs:
    c = sum(costs[key])
    if c > highestCost:
        highestCost = c
        highestMeal = key

print(highestMeal, highestCost)

lowMeal = 0
lowCost = 10000000000000

for key in costs:
    c = sum(costs[key])
    if c < lowCost:
        lowCost = c
        lowMeal = key

print(lowMeal, lowCost)

allcost = []
for key in costs:
    l = costs[key]
    allcost = allcost + l

print(min(allcost))
print(max(allcost))
print(sum(allcost))

f.close()
