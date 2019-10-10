import math
import time


def IsPrime(num):
        if num <= 1:
                return False

        if num == 2:
                return True

        if num % 2 == 0:
                return False
        
      
        i = 3
        
        for i in range(i, i <= int(math.floor(math.sqrt(num))), 2):     
                        if num % i == 0:
                                return False
                                
                        
        return True

def SequentialPrimeNumbers(num1, num2):
        
        start_time = time.time()
        
        primes = 0
       
        for i in range(num1, num2 + 1, 1):
                        print(i)
                        if IsPrime(i):
                                primes += 1
        
        elapsed_time = time.time() - start_time
        print("Duration: " + "%0.10f" % elapsed_time)
        print(primes)
        return primes

IsPrime(9)
def ParallelPrimeNumbers(num1, num2):
        pass

#SequentialPrimeNumbers(1, 10)