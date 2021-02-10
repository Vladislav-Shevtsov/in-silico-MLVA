# Search for primers in reads
bbduk_search_for_primers.py README

### Dependencies ###

python3
python-dev (sudo apt-get install python-dev), 
bbduk.sh (can be installed using conda - 
		
		conda install -c bioconda/label/cf201901 bbmap) 
		
Alternatevely, can be installed locally by downloading the source code from: 
		
		https://github.com/BioInfoTools/BBMap/blob/master/sh/bbduk.sh


### goal ###

search-primers-in-reads.py is a script with use of python language designed to automate the process of search primer sequences in reads.

This script use a list of primers in .txt file to extract only reads with located primers on both sides of the reads.


### input ###

input file with primers should have .txt extension 

example : primers_file.txt

primers format : primers name must be written as shown below in primers_file :
<primer_name>	<forward_primer>	<reverse_primer>

example : 530-insilico_3bp_46bp_2u	TAGCAGTGATACAACTTCGC	ATTAGCAGCAGGTGTACTAGATGGTCTCAATG


### output ### 

output represents files(reads) with .fastq extension which include reads containing primers on both sides of the read.    

### command line examples ###

The following command will generate .sh bash file:
python3 search-primers-in-reads.py [path/to/input.gz] [path/to/output/folder] [path/to/primers.txt]  //to generate the bash file 

The following command will execute .sh bash file:
 ./bbduk_search_primers.sh	//this will run primer search

By default 2 mismatches allowed but can be modified in the code by changing the value of mm, for example mm=3.

![Search_for_primers](https://user-images.githubusercontent.com/22825915/107493966-681fc880-6bb8-11eb-9980-6f052a15183c.jpg)
#written by Shevtsov V.
