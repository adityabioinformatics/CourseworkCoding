#!/usr/bin/env python3
# sliding_window.py

import sys

def sliding_window(k, kmer):           #Gives all the kmers input through the string
    kmers = [ ]
    end = len(kmer) - k + 1
    for start in range(0, end):
        kmers.append(kmer[start:start + k])
    return kmers

def gc_content(dna):                #Assess the GC content of the input string
    dna = dna.lower()
    gc = 0
    for nucleotide in dna:
        if nucleotide in ['g', 'c']:
            gc += 1
    return gc/float(len(dna))

if __name__ == "__main__":
    # Will raise exceptions if needed
    argv_count = len(sys.argv) - 1
    if argv_count < 2:
        raise Exception("This script requires at least 2 arguments")
    elif int(sys.argv[1]) <= 0:
        sys.exit("Value of K must be greater then Zero")
    elif int(sys.argv[1]) > len(sys.argv[2]):
        sys.exit("Value of K should be less then length of kmer given")

# getting value of k and kmer 
    k = int(sys.argv[1])
    kmer = sys.argv[2]
# passing variables
    kmers = sliding_window(k, kmer)
# printing kmer and GC content
    for km in range(len(kmers)):
        res = 0
        res = gc_content(kmers[km])
        print("{}\t{:.2f}".format(kmers[km], res))
