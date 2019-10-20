import math
import time
from multiprocessing import Pool


def returnObject(sortedNumbers, duration, method):
    return {
        "SortedNumbers": sortedNumbers,
        "Duration": duration,
        "Method": method

    }


def IsPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:

        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


def Prime(n):
    if n == 2 or n == 3:
        return n
    if n < 2 or n % 2 == 0:
        return 
    if n < 9:
        return n
    if n % 3 == 0:
        return 
    r = int(n**0.5)
    f = 5
    while f <= r:

        if n % f == 0:
            return 
        if n % (f+2) == 0:
            return 
        f += 6
    return n

def SequentialPrimeNumbers(num1, num2):
    startTime = time.time()
    Array = []
    for i in range(num1, num2, 1):
        if IsPrime(i):
            Array.append(i)

    elapsedTime = time.time() - startTime
    return returnObject(Array, elapsedTime, "Sequential")


def TaskPrime(num1, num2):
    Array = []
    for i in range(num1, num2, 1):
        if IsPrime(i):
            Array.append(i)

    return Array



def ParallelPrimeNumbers(num1, num2):
    startTime = time.time()
    m = []

    for i in range(num1,num2):
        m.append(i)
   

   
    p = Pool()
    results = p.map(Prime, m)
    results = list(filter(None.__ne__, results))
    p.close()
    elapsedTime = time.time() - startTime

    return returnObject(results, elapsedTime, "Parallel")
