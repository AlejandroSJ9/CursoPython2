import random
from re import purge

countries =['col','mex','arg']
population = {}
population_v2 = { i:random.randint(1,100) for i in countries}
print(population_v2)


result = {country : population for (country,population) in population_v2.items() if population > 20}
print(result)

text = 'Hola que mas parce'
unique = {i:c.upper() for (i,c) in text if c in 'aeiou'}
print(unique)

