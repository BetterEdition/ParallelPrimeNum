# multiproc_test.py
import time
import random
import multiprocessing


def Task(id, timeToSleep):
	
	print("Task " + str(id) + " is beginning")
	time.sleep(timeToSleep)
	print("Task " + str(id) + " has completed")


def assignTaskToProcess(nrOfTasks, timeToSleep):
    jobs = []
    for i in range(0, nrOfTasks):
        process = multiprocessing.Process(target=Task,args=(i+1, timeToSleep,))
        jobs.append(process)

    return jobs
		
    
if __name__ == "__main__":
	
	# Create a list of jobs and then iterate through
	# the number of processes appending each process to
	# the job list 

	# Arguments: Number of tasks to be created, SleepTimer
	firstTask = assignTaskToProcess(1, 3)
	
	
	# Start the processes 	
	for t in firstTask:
		t.start()
		t.join()
	
	nextTasks = assignTaskToProcess(2, 3)
	for t in nextTasks:
		t.start()
	
	for t in nextTasks:
		t.join()


	
	
	