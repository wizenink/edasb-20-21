from Bio import pairwise2
from Bio.Align import substitution_matrices
import argparse

def align(seqA,seqB,opening=11,extension=1):
    opening = -abs(opening)
    extension = -abs(extension)
    mat = substitution_matrices.load("BLOSUM62")
    alignments = pairwise2.align.globalds(seqA,seqB,match_dict=mat,open=opening,extend=extension)
    alignments.sort(key=lambda x:x.score,reverse=True)
    print(pairwise2.format_alignment(*alignments[0]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--seq1",help="Sequence 1 to pairwise-align")
    parser.add_argument("-b","--seq2",help="Sequence 2 to pairwise-align")
    parser.add_argument("--open",type=int,help="opening penalty to apply (positive or negative is irrelevant)",default=11)
    parser.add_argument("--extend",type=int,help="extension penalty to apply (positive or negative is irrelevant)",default=1)

    args = parser.parse_args()
    if(args.seq1 == None or args.seq2 == None):
        parser.print_help()
    else:
        align(args.seq1,args.seq2,args.open,args.extend)