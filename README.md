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

![107500962-fb5cfc00-6bc0-11eb-9887-c1efa8dd4dfa](https://user-images.githubusercontent.com/22825915/109280747-9b638800-7845-11eb-8a12-faec2333146b.jpg)

### input ###

input file with primers should have .txt extension 

example : primers_file.txt

primers format : primers name must be written as shown below in primers_file :
<primer_name>	<forward_primer>	<reverse_primer>

example : 530-insilico_3bp_46bp_2u	TAGCAGTGATACAACTTCGC	ATTAGCAGCAGGTGTACTAGATGGTCTCAATG

Note: It is important to make sure that you are using tab(\t) as space delimiter in Primer.txt file

### output ### 

output represents files(reads) with .fastq extension which include reads containing primers on both sides of the read.    

### command line examples ###
By default search-primers-in-reads.py recieve 3 arguments: path to input directory, path to output directory and path to file with primers.

The following command structure will generate .sh bash file:

python3 search-primers-in-reads.py [path/to/input.gz] [path/to/output/folder] [path/to/primers.txt]  //to generate the bash file 

python3 search-primers-in-reads.py ./input_data ./output_data Primers.txt

The following command will execute generated bbduk_search_primers.sh bash file:
 ./bbduk_search_primers.sh

By default 2 mismatches allowed but can be modified in the code by changing the value of mm, for example mm=3.

# Users can use and share the code freely

#For any questions please open issue on github or email me at shevtsovvladislav111@gmail.com

#written by Shevtsov V.
