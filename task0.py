def lab1(n=101):
    for i in range(n):
        number = ""
        if i % 3 == 0:
            number += "Fizz"
        if i % 5 == 0:
            number += "Buzz"
        yield number if number else i

for key, value in enumerate (lab1()):
    print(key, value)

