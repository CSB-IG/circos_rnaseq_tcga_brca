for A in basal her2 luma lumb sanos
do
    for B in basal her2 luma lumb sanos
    do
        A=`basename $A`
        B=`basename $B`
        python scatter.py data/sif_${A}.tsv data/intersect_${A}_${B}_sif.tsv
    done
done


