file = open('./text.txt')
#print(file.read())
print(file.readline())
for i in file:
  print(i)
file.close()

with open('./text.txt') as file:
  for i in file:
    print(i)
