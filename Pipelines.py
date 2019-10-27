import multiprocessing



def FindNumberToSquare(queue):
    queue.put(5)
            

def CalcSquareNumber(queue, queue2):
    number = queue.get()
    queue.close()
    queue2.put(number*number)

def ShowSquaredNumber(queue):
    print(queue.get())

def samplePipeline():
      q = multiprocessing.Queue()
      q2 = multiprocessing.Queue()
      firstTask = multiprocessing.Process(target=FindNumberToSquare, args=(q,)) 
      secondTask = multiprocessing.Process(target=CalcSquareNumber, args=(q, q2)) 
      thirdTask = multiprocessing.Process(target=ShowSquaredNumber, args=(q2,)) 

      firstTask.start()
      secondTask.start()
      thirdTask.start()

      firstTask.join()
      secondTask.join()
      thirdTask.join()

if __name__ == '__main__':
    samplePipeline()
    
