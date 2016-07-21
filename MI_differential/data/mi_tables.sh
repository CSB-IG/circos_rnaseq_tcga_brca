#awk '{print $1"\t"$2}' top_lumB_sif.tsv > top_lumB_keys.tsv

#grep -F -f top_basal_keys.tsv /mnt/e/tadeo/aracne/sanos/x.sif.txt > top_basal_keys_sanos_sif.tsv &

for KEYS in keys_basal.tsv  keys_her2.tsv  keys_lumA.tsv  keys_lumB.tsv
do
    for SIF in /mnt/e/tadeo/aracne/Basal/Basal_sif.txt \
                   /mnt/e/tadeo/aracne/Her2/Her2_sif.txt \
                   /mnt/e/tadeo/aracne/LumA/LumA_sif.txt \
                   /mnt/e/tadeo/aracne/LumB/LumB_sif.txt \
                   /mnt/e/tadeo/aracne/sanos/sanos_sif.txt
    do
        SSIF=`basename $SIF`
        grep -F -f $KEYS $SIF > intersect_${KEYS}_${SSIF}.tsv &
    done
done


