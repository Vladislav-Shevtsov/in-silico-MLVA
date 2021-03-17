# Search for primers in reads
bbduk_search_for_primers.py README

### Dependencies ###

python3
python-dev (sudo apt-get install python-dev), 

bbduk.sh (can be installed using the conda comand)
		
		conda install -c bioconda/label/cf201901 bbmap 
		
Alternatively, can be installed locally by downloading the source code from: 
		
		https://github.com/BioInfoTools/BBMap/blob/master/sh/bbduk.sh


### goal ###

search-primers-in-reads.py is a python3 script allowing to identify in a sequencing reads dataset the subset of reads containing a given pair of PCR (polymerase chain reaction) primers. 



### input ###
![Untitled-5](https://user-images.githubusercontent.com/22825915/111269219-8023b580-8658-11eb-8a29-54e54db4dfb1.jpg)

input file with primers should have .txt extension 

example: Primers.txt file

primers format: primers name must be written as shown below in Primers.txt file:
<primer_name>	<forward_primer>	<reverse_primer>

example: Ft-M22_6bp_73bp_2u	CTGCTATATTTAGACAAAGTGA	TCTGAAAGTGCTTGTTGTTGAT

Note: use tab(\t) as delimiter in Primers.txt

### output ### 

One file containing all reads in which one of the primer pairs listed in the Primers.txt is present (see Figure).  

### command line examples ###
By default search-primers-in-reads.py receive 3 arguments: path to input directory, path to output directory and path to file with primers.

The following command structure will generate .sh bash file:

```python3 search-primers-in-reads.py [path/to/input.gz] [path/to/output/folder] [path/to/Primers.txt]```  
Example:
```python3 search-primers-in-reads.py ./input_data ./output_data Primers.txt```#This will generate the bash file 

The following command will execute generated bbduk_search_primers.sh bash file:
``` ./bbduk_search_primers.sh``` #This will run bash file

By default 2 mismatches allowed but can be modified in the code by changing the value of hdist, for example hdist=3.

# Users can use and share the code freely

#For any questions please open issue on github or email me at shevtsovvladislav111@gmail.com

#written by Shevtsov V.
