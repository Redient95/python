"""
0212_id_ссылки_и_основы_модели_памяти
"""

#id()

x = 10
print(id(x))
y = 10
print(id(y))
print(id(x) == id(y))

print()

a = 5
b = a
print(id(a))
print(id(b))
print(id(a) == id(b))

print()

c = 5
d = 5
print(id(c))
print(id(d))
print(id(c) == id(d))

"""
int
float
str
bool

tuple
frozenset
"""
print()

a = 10
b = a
b = b + 1
print(a)
print(b)
print(id(a), id(b))
print(id(a) == id(b))

"""
list
dict
set
"""
print()

a = [1, 2, 3]
b = a
print(id(a), id(b))
print(id(a) == id(b))
b.append(4)
print(a)
print(b)
print(id(a), id(b))
print(id(a) == id(b))

# import copy/deepcopy copy deepcopy