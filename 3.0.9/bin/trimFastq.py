#!/opt/Python-2.6.4/bin/python
#
## this program trims fastq file to the given length
#

### import necessary libraries
import re,os,sys,logging,time,datetime;

### checking out the number of arguments
if (len(sys.argv)<4): 
  print('Not enough arguments!!');
  print ('It takes at least 3 arguments.');
  print ('Usage:\n\tProgramName inputFastq outputFastq desiredLength');
  print ('Example\n\tProgramName in.fastq out.fastq 32');
  sys.exit();

def listToString(x):
  rVal = '';
  for a in x:
    rVal += a+' ';
  return rVal;


### setting up the logging format 
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    filename='log.trimFastq.'+  str(datetime.datetime.now()),
                    filemode='w')

##### Getting Start Time ######
logging.debug('Start the program with [%s]\n', listToString(sys.argv));
startTime = time.time();

###
iFile = open(sys.argv[1]); ## input fastq file
oFile = open(sys.argv[2], 'w'); ## out fastq file
seqLen = int(sys.argv[3]); ## desira

c=0;

for line in iFile: ## for each line
  c+=1;
  if(c%2==0):  ## sequence or quality
    s = line[0:seqLen];
    oFile.write(s+'\n');
  else: ## not the sequence
    oFile.write(line);

iFile.close();
oFile.close();

#############
## calculate total running time
#############
logging.debug("Program ended");
currentTime = time.time();
runningTime = currentTime-startTime; ## in seconds
logging.debug("Program ran %.2d:%.2d:%.2d" % (runningTime/3600, (runningTime%3600)/60, runningTime%60));

sys.exit(0);
