import sys
import csv
from gene_positions import chrom
import argparse


import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Scatter plot of weights in edgelist.')
parser.add_argument('A', type=argparse.FileType('r'))
parser.add_argument('B', type=argparse.FileType('r'))
#parser.add_argument('--output', type=argparse.FileType('w'), default=sys.stdout)
args = parser.parse_args()

ra = csv.DictReader(args.A, delimiter="\t", quotechar='"')
A = {}
for e in ra:
    A[(e['from'], e['to'])] = e['weight']


rb = csv.DictReader(args.B, delimiter="\t", quotechar='"')
B = {}
for e in rb:
    B[(e['from'], e['to'])] = e['weight']


x = []
y = []
colors = []
for k in A.keys():
    if k in B:
        x.append(A[k])
        y.append(B[k])

        (s,t) = k
        # source and target in the same chromosome
        if chrom.get(s) == chrom.get(t):
            colors.append('red')
        else:
            colors.append('grey')
        

#w = csv.writer(args.output, delimiter="\t")

x = np.array(x)
y = np.array(y)

#area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses
area =50
plt.scatter(x, y, s=area, c=colors, alpha=0.4)
plt.show()

