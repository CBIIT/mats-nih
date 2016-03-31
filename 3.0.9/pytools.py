import logging, threading, Queue, traceback;
import os


if os.getenv('SLURM_CPUS_PER_TASK') != None:
    nthreads = int(os.getenv('SLURM_CPUS_PER_TASK'))
else: 
    nthreads = 1

threadQueue = Queue.Queue(nthreads)
success=0
fail=1

#Run a multithreaded list of jobs
#Input1 function to be executed list of jobs
#Input2 list of arguments to the functor as tuples
#Functions should return either success of fail. Upon reception of a failure
#function raises an exception
def executeMultithreadedJobs(functionPointer, jobList):
  """The function should accept one tuple arugment and return 0 for success for 1 for failure"""

  global threadQueue
  global success
  global fail  
  global nthreads
 
  #Run the jobs in a batch equal to the number of available threads  
  #This is done to make sure the program stops if an exception is raised
  try:
    while len(jobList)  > 0:
      toExecute = jobList[0:nthreads]
      nJobs = len(toExecute)
      threadList = []
      for thread in range(nJobs):
          t =  threading.Thread(target=functionPointer, args = toExecute[thread] )
          threadList.append(t)
          t.start()
      
      #Join the threads before continuing
      for thread in range(nJobs):
          threadList[thread].join()  
  
      #Check that all the threads executed successfully.
      if threadQueue.qsize() != nJobs:
        logging.debug("ERROR: Not all thread calls returned a value. Make sure the function returns 0 or 1")
        logging.debug("nJobs = {0}, threadQueue.qsize= {1}".format(nJobs, threadQueue.qsize()))
        exit()
      for thread in range(nJobs):
        if threadQueue.get() != success:
          logging.debug("ERROR: A thread call failed.")
          raise Exception()
  
      #Remove the executed threads from the jobList
      jobList = jobList[nJobs:] 
  except:  
    logging.debug(traceback.format_exc())
    exit()


