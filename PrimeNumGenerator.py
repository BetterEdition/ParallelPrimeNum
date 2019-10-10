import math
import time

def IsPrime(num):
        # Compute the list of all permutations of l
        # Python program to check if 
        # given number is prime or not 
        # If given number is greater than 1 
        if num > 1: 
	
        # Iterate from 2 to n / 2 
                for i in range(2, num//2): 
		
	# If num is divisible by any number between 
	# 2 and n / 2, it is not prime 
	                if (num % i) == 0: 
	                        return False
                else: 
                        return True 

        else: 
                return False


def SequentialPrimeNumbers(num1, num2):
        startTime = time.time()
        
        primes = 0
        for i in range(num1, num2, 1):
                if IsPrime(i):
                        primes += 1
                
        elapsedTime =   time.time() - startTime
        print(elapsedTime)
        return primes

def ParallelPrimeNumbers(num1, num2):
        startTime = time.time()
        
        primes = 0
        for i in range(num1, num2, 1):
                if IsPrime(i):
                        primes += 1
                
        elapsedTime =   time.time() - startTime
        print(elapsedTime)
        return primes

