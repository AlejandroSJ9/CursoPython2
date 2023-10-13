numbers = [1,2,3]
numbersv2 = []
for i in numbers:
  numbersv2.append(i*2)
print(numbersv2)

numbersv3 =list(map(lambda i:i*2, numbers))
print(numbersv3)

n1 = [1,2,3,4]
n2 = [5,6,7,8]
print(n1,'\n',n2)
v3 = list(map(lambda x,y:x*y,n1,n2))
print(v3)