#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            if i % 3 == 0 and i % 5 != 0:
                print("Fizz", end=' ')
            elif i % 5 == 0 and i % 3 != 0:
                print("Buzz", end=' ')
            else:
                print("FizzBuzz", end=' ')
        else:
            print("{}".format(i), end=' ')
