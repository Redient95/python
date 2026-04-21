"""
0209_print
"""

#print("Hello world")

name = "Ivan"
print("Hello " + name)
age = 25
print("Hello " + name + " " + str(age))

print("dsfvkmwfd\"kvmwfwfr")

print("Hello", name, False)
print("Hello", name, False, sep=' ')
print("Hello", name, False, sep='')
print("Hello", name, False, sep='---')

print()
print()
print(1, 2, 3, 4, 5, sep='-', end=', ')
print(1, 2, 3, 4, 5, sep='-', end='***')
print(1, 2, 3, 4, 5, sep='-', end='\n')
print("Hello world")
print("Hello world")

print(f'Hello {name} {age}')
print(f'Hello {name} {age + 1}')

a = 5
b = 3
print(f'{a} + {b} = {a + b}')

print(10)
print(10.1)
print(True)
print('Hello')
print([1, 2, 3])

"""
int()
float()
bool()
str()
type()
input()

a = int('5')
b = float('5.5')
c = bool(0)
d = str(5)
e = type(5)
f = input()
"""

# b = print(print())
print(b)

x = 10
y = int(input())
print("перед делением", x, y)
result = x / y

print("[DUBUG] y =", y)

# print может писать в файл
# print("текст в файле", file=f)

print(x, y, name, age, result)
print(f"Имя: {name}")
print(f"Возраст: {age}")
print(f"Возраст через год: {age + 1}")