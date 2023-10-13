dict1={}
for i in range(5):
  dict1[i] = i*2
print(dict)

dict_v2 = {i:i*2 for i in range(5)}
print(dict_v2)

country =['col','mex','arg']
population = {}

import random;
for i in country:
  population[i] = random.randint(1,100)
print(population)

population_v2 = { i:random.randint(1,100) for i in country}
print(population_v2)

names = ['nico','alejo','santi']
ages = [12,56,98]
dictionary = list(zip(names,ages))
print(dictionary)

#print(dict(list(zip(names,ages))))
new = {name : age for (name,age) in zip(names,ages)}
print(new)