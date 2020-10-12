# in-silico-MLVA
bbduk_search_for_primers.py README

### Dependencies ###

python3
python-dev (sudo apt-get install python-dev), 
bbduk.sh (can be installed using conda - 
		
		conda install -c bioconda/label/cf201901 bbmap) 
		
Alternatevely, can be installed locally by downloading the source code from: 
		
		https://github.com/BioInfoTools/BBMap/blob/master/sh/bbduk.sh


### goal ###

bbduk_search.py is a bash script with use of python language designed to automate the process of search sequences in reads.

This script use a list of primers in .txt file to recover reads with listed primers on both sides of the reads.


### input ###

input file with primers should have .txt extension 

example : primers_file.txt

primers format : primers name must be written as shown below in primers_file :
<primer_name>	<forward_primer>	<reverse_primer>

example : 530-insilico_3bp_46bp_2u	TAGCAGTGATACAACTTCGC	ATTAGCAGCAGGTGTACTAGATGGTCTCAATG


### output ### 

output represents files(reads) with .fastq extension which include reads containing primers on both sides of the read.    

### command line examples ###

python3.6 [/path/to]/bbduk_search.py //to generate the bash file 

bash bbduk_search.sh	//to run bbduk_search


#with different number of mismatch allowed :

By default 2 mismatches allowed but can be modified in the code by changing the value of mm, for example mm=3.


#written by V.Shevtsov
