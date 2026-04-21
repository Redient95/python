"""
0210_f_string_и_format
"""

name = "Вася"
age = 30
print(f"Hello, {name}! You are {age} years old.")

a = 10
b = 3
print(f"{a} / {b} = {a / b}")
print(f"Имя заглавными буквами: {name.upper()}")

import math
print(f"Площадь круга радиусом {a} = {(math.pi * a ** 2):.2f}")
print(f"{1231.123:.2f}")

print(f"|{name:10}|")
print(f"|{name:<10}|")
print(f"|{name:>10}|")
print(f"|{name:^10}|")

num = 42
print(f"{num:5}")
print(f"{num:05}")

price = 1234.5
print(f"{price:10.2f}")

value = 0.856
print(f"{value:.2%}")

print("Hello: {}".format(name))
print("Hello: {0} {1}".format(name, age))
print("Hello: {0} {0}".format(name))
print("Hello: {name} {age}".format(name=name, age=age))

print("Hello: %s" % name)
print("Hello: %s %s" % (name, age))