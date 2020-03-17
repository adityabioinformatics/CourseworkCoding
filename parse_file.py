#!/usr/bin/env python

#parse_file.py

#To use regular expressions you need to import re

import re

#Set the file path to the Drosophila genome 
dmel_genome_path= '/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta'

#Initialize a line counter
line_count= 0;

#Initialise a sequence variable 
seq= ''

with open (dmel_genome_path) as dmel_genome:
    for line in dmel_genome:
        #Increment the line counter by one
        line_count += 1
        
     #if line count is less than 5
        if line <5:
            #Check to see if the line is a header line (starts with >)
            if re.match ('^>', line):
            #print the header
                print (line)

            else:
                seq+= line

print (seq)

