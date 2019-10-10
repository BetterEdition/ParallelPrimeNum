import math


def IsPrime(num):
        primeValid = False
        if num <= 1:
                primeValid = False

        if num == 2:
                primeValid = True

        if num % 2 == 0:
                primeValid = False
        i = 3

        for i in i <= math.sqrt(num)
        if num % i == 0:
                        primeValid = True
                        break
        i += 2
        return primeValid

def main():
        print(IsPrime(3))


main()