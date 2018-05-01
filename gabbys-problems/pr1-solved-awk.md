# Pr1 Solution AWK

```
for fname in $(ls *.bam | cut -c -9 | uniq)
    do
samtools depth  -a "$fname".bam | sort -nrk3 -T /home/mgm49/scratch/tmp/ | awk -v var=$fname '
  BEGIN {
    c = 0;
    sum = 0;
  }
  $3 ~ /^[0-9]*(\.[0-9]*)?$/ {
    a[c++] = $3;
    sum += $3;
  }
  END {
    ave = sum / c;
    if( (c % 2) == 1 ) {
      median = a[ int(c/2) ];
    } else {
      median = ( a[c/2] + a[c/2-1] ) / 2;
    }
    OFS="\t";
    print var, sum, c, ave, median, a[0], a[c-1];
  }
' >> WG.stats

    done
    
    
## export
scp mgm49@login.hpc.cam.ac.uk:~/scratch/ass.studies17/BGI.sept17.1708221053/bam.files/WG.stats "Dropbox (Cambridge University)/PhD/7_Assocation_studies/4_Mydata_BGI1/depth/"


```


