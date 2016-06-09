import csv

from gene_positions import gene

with open('TablaParaCircosSanosEdge.csv') as fi, \
     open('links_sanos_same_chr.tsv', 'w') as fsame, \
     open('links_sanos_diff_chr.tsv', 'w') as fdiff:
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




