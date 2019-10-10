import PrimeNumGenerator
import multiprocessing as mp


def startPrimeNumConsole():
    print('input number, to check if the number is a Prime!')
    number = int(input()) 
    isPrime = PrimeNumGenerator.IsPrime(number)
    print(isPrime)


def sequentialPrimeNumbers():
    
    print('input 2 number, to get the amount of primes between these numbers')
    print('input first number..')
    firstNumber = int(input()) 
    print('input secound number..')
    secoundNumber = int(input()) 
    primeNumbers = PrimeNumGenerator.SequentialPrimeNumbers(firstNumber,secoundNumber)
    print(primeNumbers)



startPrimeNumConsole()


sequentialPrimeNumbers()