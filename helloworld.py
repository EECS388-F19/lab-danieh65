from random import randint

name = "Daniel"
print(name)

first = randint(0, 101)
print(first)
second = randint(0, 101)
print(second)

sum = first + second
print(str.format("Sum = {}", sum))

mean = sum / 2
print(str.format("Average = {}", mean))
