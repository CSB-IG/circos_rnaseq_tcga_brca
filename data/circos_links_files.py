import csv

from gene_positions import gene

for status in ('sanos', 'enfermos'):
    with open('%s_edges.csv' % status) as fi, \
         open('links_%s_same_chr.tsv' % status, 'w') as fsame, \
         open('links_%s_diff_chr.tsv' % status, 'w') as fdiff:
        csvr     = csv.DictReader(fi)
        same_chr = csv.writer(fsame, delimiter='\t')
        diff_chr = csv.writer(fdiff, delimiter='\t')

        for row in csvr:
            (s,w,t)=row['name'].split()
            try:
                source = gene[s]
                target = gene[t]
            except:
                continue

            if source[2] == target[2]:
                same_chr.writerow(["hs%s" % source[2], source[0], source[1], "hs%s" % target[2], target[0], target[1]])
            else:
                diff_chr.writerow(["hs%s" % source[2], source[0], source[1], "hs%s" % target[2], target[0], target[1]])




