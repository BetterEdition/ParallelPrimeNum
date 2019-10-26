import time
from multiprocessing import Pool

work = (["W", 10], ["X", 2], ["Y", 2], ["Z", 2])

def worker(work_data):
    print(" Process %s waiting %s seconds" % (work_data[0], work_data[1]))
    time.sleep(int(work_data[1]))
    print(" Process %s Finished." % work_data[0])
    return 'done' + work_data[0]

def poolHandler():
    p = Pool(2)
    result = p.map(worker, work)

    print(result)

if __name__ == '__main__':
    poolHandler()