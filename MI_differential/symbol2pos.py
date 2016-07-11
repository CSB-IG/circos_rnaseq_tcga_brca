import sys
import csv
from gene_positions import gene as pos
import argparse

parser = argparse.ArgumentParser(description='Replace gene symbol by chr-start-end. Output TSV file.')
parser.add_argument('--input', type=argparse.FileType('r'), required=True)
parser.add_argument('--output', type=argparse.FileType('w'), default=sys.stdout)
args = parser.parse_args()

r = csv.DictReader(args.input, delimiter="\t", quotechar='"')
w = csv.writer(args.output, delimiter="\t")

for e in r:
    if e['from'] in pos and e['to'] in pos:
        (from_start, from_end, from_chrom) = pos[e['from']]
        (to_start,   to_end,   to_chrom)   = pos[e['to']]
        link = ["hs%s" % from_chrom, from_start, from_end,
                "hs%s" % to_chrom,   to_start,   to_end,
                e['weight']]
        w.writerow(link)
