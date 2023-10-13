array = []
for element in range(11):
  array.append(element * 2)

print(array)

numbers_v2 = [element  for element in range(11) if element % 2 == 0]
print(numbers_v2)