from difflib import ndiff
import argparse
from Bio import pairwise2
from Bio.Align import substitution_matrices


#NON-PAIRWISE2 implementation. currently not being used
def levenshtein_distance(seqA, seqB):
    distance = 0
    ops = {"+":0, "-":0}
    buffer_removed = buffer_added = 0
    for x, *_ in ndiff(seqA, seqB):
        if x == '?':
            continue
        elif x == ' ':
            distance += max(ops.values())
            ops = {"+":0, "-":0}
        else:
            ops[x] +=1
    distance += max(ops.values())
    return distance

def distance(seqA,seqB):
    alignments = pairwise2.align.globalms(seqA,seqB,0,-1,open=-1,extend=-1)
    alignments.sort(key=lambda x:x.score)
    return int(-alignments[0].score)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--seq1",help="Sequence 1")
    parser.add_argument("-b","--seq2",help="Sequence 2")
    args = parser.parse_args()
    if(args.seq1 == None or args.seq2 == None):
        parser.print_help()
    else:
        print(distance(args.seq1,args.seq2))