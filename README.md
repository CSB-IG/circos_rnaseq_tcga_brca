# RNASeq interactions from TCGA BRCA samples

A nice observation: RNAseq interactions on healthy tissue are mostly
interchromosomic, whereas in tumor tissue they are mostly
intrachromosomic.

           | healthy | tumor
-----------|---------|------
same chrom | 1473    | 11040
diff chrom | 9801    | 266


<table>
<tr>
<td><img src="circos_sanos.png" width="100%">A. Healthy tissue</td>
<td><img src="circos_enfermos.png" width="100%">B. Tumor tissue</td>
</tr>
</table>

Shown in red are the node degrees in the interaction network. The tumor plot also shows differential expression profiles in the outermost ring. 
