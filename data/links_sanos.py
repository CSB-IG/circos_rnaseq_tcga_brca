import csv

from gene_positions import gene

with open('TablaParaCircosSanosEdge.csv') as f:
    csvr = csv.DictReader(f)
    for row in csvr:
        (s,w,t)=row['name'].split()
        try:
            print "hs%s" % gene.get(s)[2], gene.get(s)[0], gene.get(s)[1], "hs%s" % gene.get(t)[2], gene.get(t)[0], gene.get(t)[1]
        except:
            pass
