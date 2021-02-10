import csv
import os
import sys

#determine tool directories
#bbduk = '/home/vladislav.shevtsov/miniconda3/envs/mlvapython3/bin/bbduk.sh'


#determine files directories
data_in_dir = sys.argv[1]
data_out_dir = sys.argv[2]

fastq_gz_row_list = sorted([os.path.join(data_in_dir, i) for i in os.listdir(data_in_dir) if i.endswith('.gz')])

def generate_bbduk_output_name(name, suffix = 'OUT'):
    a, b = os.path.splitext(name)
    new_name = a + '_'+ suffix + b
    return new_name

doc= sys.argv[3]
#lines=doc.readlist()
#print(lines[2])

bash_file = 'bbduk_search_primers.sh'
with open(bash_file, 'w') as f, open(doc,'r') as primer:
    file_reader=csv.reader(primer,delimiter='\t')
    f.write('#!/bin/bash \n')
    for lines in file_reader:
        #print(len(lines[1]))
        for sample in fastq_gz_row_list:
            name = os.path.basename(sample)
            name, _ = os.path.splitext(name)
            out_sample = os.path.join(data_out_dir, name)
            out_sample = generate_bbduk_output_name(out_sample, lines[0])
            out_sample2 = generate_bbduk_output_name(out_sample)
            #print(out_sample)
            if not os.path.isfile(out_sample):
              f.write(f'bbduk.sh in={sample} outm={out_sample} literal={lines[1]} mm=f k=19 minlen=1 hdist=2 forbidn=t threads=38 \n')
              f.write(f'bbduk.sh in={out_sample} outm={out_sample2} literal={lines[2]} mm=f k=19 minlen=1 hdist=2 forbidn=t threads=38 \n')
              f.write(f'rm {out_sample} \n' )
