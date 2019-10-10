import math
import time

input1 = 1
input2 = 100000

def IsPrime(num):
        primeValid = True
        if num <= 1:
                primeValid = False

        if num == 2:
                primeValid = True

        elif num % 2 == 0:
                primeValid = False
        
        i = 3
        
        for i in range(i, int(math.floor(math.sqrt(num))), 2):
                        if num % i == 0:
                                primeValid = False
                                break
                        
        return primeValid

def SequentialPrimeNumbers(num1, num2):
        now = time.time
        primes = 0
        i = 0
        for i in range(num1, i <= num2, 1):
                if IsPrime(i):
                        primes + 1
        
        return primes
