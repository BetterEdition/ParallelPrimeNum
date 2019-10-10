import PrimeNumGenerator
from tkinter import *


#"SortedNumbers": sortedNumbers,
 #   "Duration": duration,
  #  "Method": method


window = Tk()
def sequentialPrimeNumbers(firstNumber, secondNumber):
    global window
    primeNumbers = PrimeNumGenerator.SequentialPrimeNumbers(int(firstNumber), int(secondNumber))
    
    t = Text(window)
    t.delete('1.0', END)
    t.insert(END, "Approach: " + primeNumbers["Method"] + '\n')
    t.insert(END, "Time: " + str(primeNumbers["Duration"])  + '\n')
    t.insert(END, "The following numbers are primes:" + '\n')
    for x in primeNumbers["SortedNumbers"]:
        t.insert(END, str(x) + '\n')
    t.pack()
    window.mainloop()

    
def parallelPrimeNumbers(firstNumber, secondNumber):
    
    global window
    primeNumbers = PrimeNumGenerator.ParallelPrimeNumbers(int(firstNumber), int(secondNumber))
    t = Text(window)
    t.delete('1.0', END)
    t.insert(END, "Approach: " + primeNumbers["Method"] + '\n')
    t.insert(END, "Time: " + str(primeNumbers["Duration"])  + '\n')
    t.insert(END, "The following numbers are primes:" + '\n')
    for x in primeNumbers["SortedNumbers"]:
       
        t.insert(END, str(x) + '\n')
    t.pack()
    window.mainloop()


def text():
    print(10)

def CreateUI():
    global window
   
    canvas1 = Canvas( width = 400, height = 300)
    canvas1.pack()
    
    

    input1 = Entry(window, width=10)
    input2 = Entry(window, width=10)
    
    canvas1.create_window(200, 140, window=input1)
    canvas1.create_window(200, 160, window=input2) 
    button1 = Button(window,text='Sequential', width=50, command=lambda: sequentialPrimeNumbers(int(input1.get()), int(input2.get())))
    button2 = Button(window,text='Parallel', width=50, command=lambda: parallelPrimeNumbers(int(input1.get()), int(input2.get())))
    
    canvas1.create_window(200, 250, window=button1)
    canvas1.create_window(200, 200, window=button2)
    window.mainloop() 




if __name__ == '__main__':
    CreateUI()

