#
### test run for MATS
### 
# Check for proper number of command line args.
#
EXPECTED_ARGS=1
E_BADARGS=65

if [ $# -ne $EXPECTED_ARGS ]
then
  echo "Usage: `basename $0` bowtieIndex"
  echo "Example: `basename $0` ~/bowtieIndexes/hg19"
  exit $E_BADARGS
fi
#
#
### test it with bam files
#
echo "Testing MATS with BAM input files"
#
python RNASeq-MATS.py -b1 testData/231ESRP.25K.rep-1.bam,testData/231ESRP.25K.rep-2.bam -b2 testData/231EV.25K.rep-1.bam,testData/231EV.25K.rep-2.bam -gtf testData/test.gtf -o bam_test -t paired -len 50 -a 8 -c 0.0001 -analysis U -keepTemp
#
### test with fastq files and bowtie indexes
#
#
echo " "
echo "Testing MATS with FASTQ input files.." 
echo "This step involves mapping to GTF and could take up to an hour.."
#
python RNASeq-MATS.py -s1 testData/231ESRP.25K.rep-1.R1.fastq:testData/231ESRP.25K.rep-1.R2.fastq,testData/231ESRP.25K.rep-2.R1.fastq:testData/231ESRP.25K.rep-2.R2.fastq -s2 testData/231EV.25K.rep-1.R1.fastq:testData/231EV.25K.rep-1.R2.fastq,testData/231EV.25K.rep-2.R1.fastq:testData/231EV.25K.rep-2.R2.fastq -gtf testData/test.gtf -bi $1 -o out_test -t paired -len 50 -a 8 -r1 72,75 -sd1 40,35 -r2 70,65 -sd2 48,45 -c 0.0001 -analysis U -keepTemp
###
echo " "
echo "Testing MATS finished.." 
#
