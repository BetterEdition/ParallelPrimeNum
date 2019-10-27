# multiproc_test.py
import time
import random
import multiprocessing


def Task(id, timeToSleep, Token):
	print("Task " + str(id) + " is beginning")
	if(timeToSleep > 5):
		Token.value = False
	
	if(Token.value):
		time.sleep(timeToSleep)
		print("Task " + str(id) + " has completed")
	else:
		print("The timeToSleep is too time consuming, cancelling task")
		
		
	

def assignTaskToProcess(nrOfTasks, timeToSleep, Token):
    jobs = []
    for i in range(0, nrOfTasks):
        process = multiprocessing.Process(target=Task,args=(i+1, timeToSleep, Token))
        jobs.append(process)

    return jobs
		
    
if __name__ == "__main__":
	
	# Create a list of jobs and then iterate through
	# the number of processes appending each process to
	# the job list 

	# Arguments: Number of tasks to be created, SleepTimer
	Token = multiprocessing.Value('b', True)
	firstTask = assignTaskToProcess(1, 6, Token)
	
	# Start the processes
	for t in firstTask:
		t.start()
		t.join()
	
	while Token.value:
		nextTasks = assignTaskToProcess(2, 3, Token)
		for t in nextTasks:
			t.start()
	
		for t in nextTasks:
			t.join()
		break


	
	
	