import csv
import os


#determine tool directories
bbduk = '/path_to/bbduk.sh' #change to bbduk.sh location

#determine files directories
data_in_dir = '/path_to/input_data' #change to input folder
data_out_dir = '/path_to/output_data' #change to output folder
#determine list of files
fastq_gz_row_list = sorted([os.path.join(data_in_dir, i) for i in os.listdir(data_in_dir) if i.endswith('.gz')])
#generate output name with suffix
def generate_bbduk_output_name(name, suffix = 'OUT'):
    a, b = os.path.splitext(name)
    new_name = a + '_'+ suffix + b
    return new_name
#determine primer location
doc='path_to/Primer_list.txt' #change to primer location

#determine the name of executable bash file 
bash_file = 'search_primers.sh' #Name of executable file - Can be modified
with open(bash_file, 'w') as f, open(doc,'r') as primer:
    file_reader=csv.reader(primer,delimiter='\t')
    f.write('#!/bin/bash \n')
    for lines in file_reader:
        
        for sample in fastq_gz_row_list:
            name = os.path.basename(sample)
            name, _ = os.path.splitext(name)
            out_sample = os.path.join(data_out_dir, name)
            out_sample = generate_bbduk_output_name(out_sample, lines[0])
            out_sample2 = generate_bbduk_output_name(out_sample)
            #print(out_sample)
            if not os.path.isfile(out_sample):
              f.write(f'{bbduk} in={sample} outm={out_sample} literal={lines[1]} mm=f k=20 minlen=1 hdist=2 forbidn=t threads=38 \n')
              f.write(f'{bbduk} in={out_sample} outm={out_sample2} literal={lines[2]} mm=f k=20 minlen=1 hdist=2 forbidn=t threads=38 \n')
              f.write(f'rm {out_sample} \n' )
