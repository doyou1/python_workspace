import numpy as np

a = {'a' : 0, 'b':1, 'c':2}

# for attr in dir(a):
#     print(attr)

a = 10
# print(id(a))

a = 20
# print(id(a))

a = np.array([1,2,3])
b = [1,2,3]
c = (1,2,3)
print(type(a))
for attr in dir(a):
    if not attr.startswith('__'):
        print(attr)

print(type(b))
for attr in dir(b):
    if not attr.startswith('__'):
        print(attr)

print(type(c))
for attr in dir(c):
    if not attr.startswith('__'):
        print(attr)

x = {'a' : 1, 'b' : 2}
y = {'b' : 3, 'c' : 4}

z = {**x, **y}

print(z)

a = [1,2,3]
b = [4,5,6]

print("enumerate(a+b)")
for index, value in enumerate(a+b):
    print(index,value)

print("enumerate(zip(a+b))")
for index, value in enumerate(zip(a+b)):
    print(index,value)


print(zip(a))