
# Will create this

# hs6 30844198 30867933 0.949201096539538
# hs7 73645829 73668774 0.529426928008456
#hs1 161576081 161578007 -0.319124653818656


import csv
from gene_positions import gene

with open('enfermos_nodes.csv') as f, \
     open('hist_degree.tsv', 'w') as deg, \
     open('hist_lratio.tsv', 'w') as rat:
        csvr     = csv.DictReader(f)
        degw = csv.writer(deg, delimiter='\t')
        ratw = csv.writer(rat, delimiter='\t')        

        for row in csvr:
            try:
                (start, end, chrom) = gene[row['shared name']]
                lratio              = row['Exp Log Ratio']
                degree              = row['Node Degree']
            except:
                continue            

            degw.writerow(["hs%s" % chrom, start, end, degree])
            ratw.writerow(["hs%s" % chrom, start, end, lratio])
