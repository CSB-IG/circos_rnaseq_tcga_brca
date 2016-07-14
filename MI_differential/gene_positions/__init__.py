import csv

grch37 = csv.DictReader(open('gene_positions/grch37_gene_positions.tsv'), delimiter="\t")

chrom = {}
for gene in grch37:
    chrom[gene['Symbol']] = gene['Chromosome']
