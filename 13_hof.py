f1 = lambda x : x + 2
f2 = lambda x, func : x + func(x)

print(f2(2,lambda x: x*3))

