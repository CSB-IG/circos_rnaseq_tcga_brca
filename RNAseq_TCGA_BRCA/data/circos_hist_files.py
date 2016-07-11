import csv
from gene_positions import gene

with open('enfermos_nodes.csv') as f, \
     open('hist_enfermos_degree.tsv', 'w') as deg, \
     open('hist_lratio.tsv', 'w') as rat:
        csvr     = csv.DictReader(f)
        degw = csv.writer(deg, delimiter='\t')
        ratw = csv.writer(rat, delimiter='\t')        

        for row in csvr:
            try:
                (start, end, chrom) = gene[row['shared name']]
                lratio = row['Exp Log Ratio']
                if lratio == "":
                    lratio = 0
                degree = row['Node Degree']
                if degree == "":
                    degree = 0
            except:
                continue            

            degw.writerow(["hs%s" % chrom, start, end, degree])
            ratw.writerow(["hs%s" % chrom, start, end, lratio])



with open('sanos_nodes.csv') as f, \
     open('hist_sanos_degree.tsv', 'w') as deg:
        csvr     = csv.DictReader(f)
        degw = csv.writer(deg, delimiter='\t')

        for row in csvr:
            try:
                (start, end, chrom) = gene[row['shared name']]
                degree = row['Node Degree']
                if degree == "":
                    degree = 0
            except:
                continue            

            degw.writerow(["hs%s" % chrom, start, end, degree])            
