samples = ['basal', 'her2', 'luma', 'lumb', 'sanos']
print "<table>"
for i in samples:
    print "<tr><td>x=%s</td>" % i
    for j in samples:
        print "<td>y=%s" % j
        print "<img src='sif_%s.tsv_intersect_%s_%s_sif.tsv.png'>" % ( i, i, j)
        print "</td>"
    print "</tr>"
print "</table>"
        
