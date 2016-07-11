import argparse
import csv

parser = argparse.ArgumentParser(description='Compute genomic distance distribution of same chromosome circos links file.')
parser.add_argument('links', type=argparse.FileType('r'))
args = parser.parse_args()

linksr = csv.reader(args.links, delimiter="\t")

def distance(s_start, s_end, t_start, t_end):
    if s_end < t_start:
        return t_start-s_end
    elif t_end < s_start:
        return s_start - t_end
    elif t_start > s_start:
        return t_start - s_start
    else:
        return s_start - t_start
    
for l in linksr:
    (s_chr, s_start, s_end, t_chr, t_start, t_end) = l
    print distance(int(s_start), int(s_end), int(t_start), int(t_end))
