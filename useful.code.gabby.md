# Useful code

## Logins CSD3


**Note for new users:** raven password must be STRONG, or you wont be allowed to log in- it will not give an explicative warning either

```
**# NEW login to CSD3
 ssh mgm49@login-cpu.hpc.cam.ac.uk
 
**
# login to butterfly and darwin- DEPRECATED
ssh -X mgm49@login-butterfly1.hpc.cam.ac.uk
 
# butterfly login once already in the cluster
ssh login-butterfly1

```

## Program loading/finding

For installing check [Downloading](https://quip.com/QpJYAfbcsswG) 

```
# check whats on the system (environment)
modules
module avail

# check what you have loaded
module list

#load program on the system
module load samtools


```

## Copying

```
# to copy from server to local
scp mgm49@login-cpu.hpc.cam.ac.uk:~/rds/rds-cj107-heliconius/Jiggins/Novogene2018_C101HW17120109/file.structure.Novogene2018_C101HW17120109.txt "Dropbox (Cambridge University)/PhD/7_Assocation_studies/file.structure.Novogene2018_C101HW17120109.txt"


# from local to server
scp -P 22 "Dropbox (Cambridge University)/PhD/7_Assocation_studies/1_Nadeau14_data/test_16march/list_test_runs.txt" mgm49@login.hpc.cam.ac.uk:~/scratch/nadeau14/

scp  -r -v -P 22 ~/../../Volumes/My\ Passport/CAM*  mgm49@login.hpc.cam.ac.uk:~/rds/rds-cj107-heliconius/mgm49/micro.ct.Heli/malleti/

#to copy files according to a list (listtestruns) to a different location. you need to be within the directory where the files are
cat ../list_test_runs.txt | xargs mv -t ../test_data160317

cat paths.txt | xargs -I % cp -R % ./

# different options
cat ../../../../PhD/7_Assocation_studies/7_Nic_highcov_Novogene/nic_photos/image.list.txt | xargs mv -t ../../../../PhD/7_Assocation_studies/7_Nic_highcov_Novogene/nic_photos

cat ../../../../PhD/7_Assocation_studies/7_Nic_highcov_Novogene/nic_photos/image.list.txt | xargs -J % echo cp % ../../../../PhD/7_Assocation_studies/7_Nic_highcov_Novogene/nic_photos/

cat ../image.names.batch2.txt | xargs -J % scp % ../input.batch2/

cat ~/Dropbox/PhD/12_coll_GMK/photo.id/sara.id/sara.names.txt | xargs -J % scp % ~/Dropbox/PhD/12_coll_GMK/photo.id/sara.id/

cat to.copy.gabby.txt | xargs -I % cp % ~/rds/hpc-work/ass.studies17/BGI.jan.18/raw.tidy/

xargs -a to.copy.gabby.txt cp -t ~/rds/hpc-work/ass.studies17/BGI.jan.18/raw.tidy/

`cp F* -t /home/mgm49/rds/hpc-work/ass.studies17/BGI.jan.18/raw.tidy/

for file in $(<to.copy.gabby.txt); do cp "$file" /home/mgm49/rds/hpc-work/ass.studies17/BGI.jan.18/raw.tidy/; done`
```





```
# to copy all contents to another folder
cp -a raw_data/. data/

# to remove file that starts with wildcard
rm \*.fastq.gz

# To remove the folder with all its contents(including all interior folders):
rm -rf /path/to/directory

# To remove all the contents of the folder(including all interior folders) but not the folder itself:
rm -rf /path/to/directory/*

# To remove all the files from inside a folder(not removing interior folders:
rm -f /path/to/directory/*

# change directory name to just 9 first characters:`
for f in CAM*
do
    mv "$f" "${f:0:9}"
done`


 
```

## Permissions


getent group heliconius

```
# to make sure all group can
chgrp -R heliconius sequencing_data/
chmod -R ug+rwx

-rw-r--r-- 1 iaw22 iaw22 1178579738 Feb 22 13:37 FCHJMGLCCXY_L4_CAM040433_1.fq.gz
```

```
#permissions
 ls -lh -ld  Novogene2017_C101HW17060384/
 ls -lh
 
# check group members
getent group butterfly
butterfly:*:8042:alp66,jd626,jjh55,mm2083,pmr47,rwrw2,sjr20,smf34,jcjb,shm45,eh481,cr600,wrk21,lh588

getent group heliconius
heliconius:*:8036:jd626,alp66,shm45,rmm60,jjh55,eh481,mm2083,sv378,cr600,mgm49,lh588,cj107,iaw22,heliconius-webdav

# modifying permissions/rights of a directory, 

chmod -R ug+rwx Novogene2017_C101HW17060384/
chmod -R g-w ./
chmod ug+rwx *.bam

# for modifying ownership use chown 
chown

# change group of directory
chgrp heliconius ./

```

[Image: file:///-/blob/eTYAAAZPjFW/Spyi2qCZJvMqs_fNBVDx_A]
https://boinc.berkeley.edu/wiki/Linux_file_permissions

https://www.linux.com/LEARN/HOW-MANAGE-FILE-AND-FOLDER-PERMISSIONS-LINUX

## Inspecting directories

```

#list contents of dirctory
ls -1  tim.cropped/

#count files in directory
ls | wc -l

#size of directory
du -h
du -sh
du -sh *
du -sk * | sort -n

#number of lines in file
wc -l file

# print columns one and ten in a space delimited file made with nano
awk -F ' ' '{print $1, $10}' erato.samples.Col.E.info

#check your space
quota
```

## Inspecting files

```
`# inspect backwards (less)
tac filename | less

`
```

## Submitting jobs to CSD3

Paid account
Must submit from hpc-work (your scratch)

https://www.csd3.cam.ac.uk/using-clusters/running-jobs/submission

```
ssh mgm49@login.hpc.cam.ac.uk

# script skeleton 

#create script
nano 1.script.txt

# script skeleton

#!/bin/bash
#SBATCH -J 1.sfs
#SBATCH -o slurm.sfs-%j.out
#SBATCH -e slurm.sfs-%j.out
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --tasks=32
#SBATCH -p skylake
#SBATCH --exclusive

#command goes here

mkdir helloworld

END=$(date +%s)
echo "End time: `date`"
RUNSECONDS=$(($END - $START))
RUNHOURS=$(($RUNSECONDS/3600))
RUNMINUTES=$((($RUNSECONDS-($RUNHOURS*3600))/60))
printf "Run time for $1.$2.$3 against $6 : %3d:%02d\n" "$RUNHOURS" "$RUNMINUTES"

#submit script to cluster
```````````sbatch -A JIGGINS-SL2-CPU 1.script.txt
````````````````````````
#check process
squeue -u mgm49`````````````

# to submit script, free (can take days). make sure time limits, nodes are low
sbatch realSFS1_submit.txt

# to check when job will start
squeue -u mgm49 --start

# to cance job
scancel JOBIB

# check cpu hours left
mybalanace



# check cluster details
grep "physical id" /proc/cpuinfo | sort | uniq | wc -l
 2
grep ^processor /proc/cpuinfo | wc -l
 32
grep 'cpu cores' /proc/cpuinfo | sort | uniq
 cpu cores    : 16
 
 
```




## CSD3 submission templates

```
# Template submission scripts can be found for each of the three
# new clusters under 

/usr/local/Cluster-Docs/SLURM:

slurm_submit.peta4-skylake
slurm_submit.peta4-knl
slurm_submit.wilkes2


```

## Submitting memory heavy jobs to CSD3

Use himem partition (https://www.csd3.cam.ac.uk/using-clusters/running-jobs/submission )


```
#SBATCH -p skylake-himem


```

```
#submit script to cluster
```````````sbatch -A JIGGINS-SL2-CPU```````````
```

and will be allocated the number of CPUs required for the number of tasks requested and a corresponding amount of memory.
By default, the **skylake** partition provides 1 CPU and **5990MB** of RAM per task, and the **skylake-himem** partition provides 1 CPU and **12040MB** per task.


Reply from Steven (example skeleton):


> This would e the max you can run:

> 

> #!/bin/bash
#SBATCH -p skylake-himem
#SBATCH --ntasks=1
#SBATCH --time=12:00:00
#SBATCH --cpus-per-task=32
#SBATCH -A JIGGINS-SL3-CPU


> 32x12gb = 384gb RAM

```
[mgm49@login-e-16 12.e.cyr.EhighW.ElowW.BGI.042018]$ squeue -u mgm49
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
           1491301 skylake-h    1.sfs    mgm49  R       0:09      1 cpu-e-404
           
           
```

## Running jobs in Butterfly

Submitting jobs to butterfly. Free for Heliconius lab. For jobs that are only 1 task, faster than CSD3. But in CSD3 you can run many jobs in parallel.

```
# login to butterfly and darwin
ssh -X mgm49@login-butterfly1.hpc.cam.ac.uk

#login to butterfly (from darwin)
ssh login-butterfly1
```````
# submitting scripts to butterfly (must be .sh)
nohup bash `````````WG.stats`````````.sh &
```````
# submit commands (send to background)
nohup [command] &

# check usage
module load htop
htop #check taht overall mem is not too high
top

# to check progress
ps -fumgm49

kill [jobID]

bg



```






## Sending jobs to background

So that if your session stops (computer turning off for example) it carries on


```
control+z to pause the job
bg #send it to background
jobs

#check that background jobs are running
ps -fumgm49

# stop background job
kill [PID number]
```



## Scratch

scratch: 1TB for each user
zip stuff

new scratch

```
cd home/rds/hpc-work/
```

## My usage

```
quota
mybalance
gbalance
gstatement

```



## RCS


Research Cold Storage 30TB. slower.
Trick to get files faster: .tar files together (from a same project for example) so that it is easier for the system to find the files
I have

rcs: 30TB, slower cold storage, for backup. tar files so that there is only one start position in the rds

two subdirectories that are linked (what happens in one happen in the other):

* rcs-cj107 - heliconius with individual directories for each member of the lab → full permission within my directory
* heliconius-cj107 - 

Do not mv (move) files out of cold storage. If you need a file for analyses scp to your scratch.

## RDS


10TB
Research data storage
rds: for files that we are sharing with other labs 10TB

To give access to data to external users:


> This has been done at;
https://jiggins-dav.vss.cloud.cam.ac.uk/webdav
Alternatively, it can be mounted over DAVS as;
davs://[jiggins-dav.vss.cloud.cam.ac.uk/webdav](http://jiggins-dav.vss.cloud.cam.ac.uk/webdav)
The credentials for the read-only user are;
Username: read-only
Password: Priest-Reason-Cultivate-Jump-4



## 
R

```
module load R
R
> getwd()
> quit()
```



## Copying sequenced genomes from Hard drive

```
pwd #to see what path the directory is

#test by coying ony the pdf help file 

scp -P 22 cd SSeagate\ Backup\ Plus\ Drive/C101HW17060384/C101HW17060384/clean_data/Cleandata_Readme.pdf mgm49@login.hpc.cam.ac.uk:~/rds/rds-cj107-heliconius/Jiggins/Novogene2017_C101HW17060384/

scp -P 22 ~/../../Volumes/Seagate\ Backup\ Plus\ Drive/C101HW17060384/C101HW17060384/clean_data/ mgm49@login.hpc.cam.ac.uk:~/rds/rds-cj107-heliconius/Jiggins/Novogene2017_C101HW17060384/

#secure copy all folders and contents within -r - NOT WORKING
scp  -r -P 22 ~/../../Volumes/Seagate\ Backup\ Plus\ Drive/C101HW17060384/C101HW17060384/clean_data/ mgm49@login.hpc.cam.ac.uk:~/rds/rds-cj107-heliconius/Jiggins/Novogene2017_C101HW17060384/clean_data/


```

```

#test copy one sample from home directrory ro rcs - works and progress shown
scp  -r -v -P 22 "Dropbox (Cambridge University)/PhD/7_Assocation_studies/2_Colombia_high.depth/backup/clean_data/CAM15072/" mgm49@login.hpc.cam.ac.uk:~/rcs/rcs-cj107-heliconius/mgm49/Novogene2017_C101HW17060384/clean_data/

# all clean_data to RCS
scp  -r -v -P 22 "Dropbox (Cambridge University)/PhD/7_Assocation_studies/2_Colombia_high.depth/backup/clean_data/" mgm49@login.hpc.cam.ac.uk:~/rcs/rcs-cj107-heliconius/mgm49/Novogene2017_C101HW17060384/clean_data/

# all clean_data to RDS
scp  -r -v -P 22 "Dropbox (Cambridge University)/PhD/7_Assocation_studies/2_Colombia_high.depth/backup/clean_data/" mgm49@login.hpc.cam.ac.uk:~/rds/rds-cj107-heliconius/Jiggins/Novogene2017_C101HW17060384/clean_data/


```

Emma Curran's data 

```
#secure copy all folders and contents within -r - (works)
scp  -r -P 22 ~/../../Volumes/TOSHIBA\ EXT/sheffield/ mgm49@login.hpc.cam.ac.uk:~/rcs/heliconius-cj107/mgm49/curran_nadeau_160310_westCol_westEc/

```

 Novogene 2018 nic high depth

```
# all clean_data to RDS- for sharing
 scp -r -v  ~/../../Volumes/Seagate\ Backup\ Plus\ Drive/C101HW17120109/data_result/C101HW17120109/clean_data/C_041* mgm49@login-cpu.hpc.cam.ac.uk:/home/mgm49/rds/rds-cj107-heliconius/Jiggins/Novogene2018_C101HW17120109/clean_data/

# all clean_data to RCS- for storing
 scp -r -v  ~/../../Volumes/Seagate\ Backup\ Plus\ Drive/C101HW17120109/data_result/C101HW17120109/clean_data/ mgm49@login-cpu.hpc.cam.ac.uk:/home/mgm49/rcs/rcs-cj107-heliconius/mgm49/Novogene2018_C101HW17120109/
 
 
 
 
 
 mgm49@login.hpc.cam.ac.uk:~/rds/rds-cj107-heliconius/Jiggins/Novogene2017_C101HW17060384/clean_data/
```




## **FTP downloading genomes from BGI**


Website: http://cdts-hk.genomics.cn/
Username: 20170927F17FTSEUHT0840bycyq
Password: BUTwqtRbycyq

Login  http://cdts-hk.genomics.cn/
Instructions http://cdts-hk.genomics.cn/customerSupport/HowToDownloadDataFromCDTS.pdf

wget http://cdts-hk.genomics.cn/img/data/icon/data_folder.gif

```
# check the ftp path of one file  on a  browser
ftp://20170927F17FTSEUHT0840bycyq:BUTwqtRbycyq@cdts-hk.genomics.cn/F17FTSEUHT0840_BUTwqtR/md5.check

# adapt it to test with 1 file
wget ftp://20170927F17FTSEUHT0840bycyq:BUTwqtRbycyq@cdts-hk.genomics.cn/F17FTSEUHT0840_BUTwqtR/md5.check

# make it recursive so that it copies everything -voila. submit to butterfly if many files
wget -r ftp://20170927F17FTSEUHT0840bycyq:BUTwqtRbycyq@cdts-hk.genomics.cn/F17FTSEUHT0840_BUTwqtR/

# if not on file path must specify ftp user pw
wget ‐‐ftp-user=20170927F17FTSEUHT0840bycyq ‐‐ftp-password=BUTwqtRbycyq ftp://20170927F17FTSEUHT0840bycyq:BUTwqtRbycyq@cdts-hk.genomics.cn/F17FTSEUHT0840_BUTwqtR/md5.check


```




## SFTP download STRI server

```
sftp://globus.si.edu/public/KK_GMK

http://globus.si.edu/public/KK_GMK

# if not on file path must specify ftp user pw
wget ‐‐ftp-user=sftp ‐‐ftp-password=sftp123! sftp://globus.si.edu/public/KK_GMK/colombia.log

wget sftp://globus.si.edu/public/KK_GMK/colombia.log

scp -p 22 sftp@globus.si.edu:/public/KK_GMK/colombia.log mgm49@login.hpc.cam.ac.uk:~/rcs/rcs-cj107-heliconius/mgm49/kozak.erato.melp.feb.2018

# none of the above worked
# solution, from https://www.tecmint.com/sftp-command-examples/
1. login to darwin
2. go to desired destination directory
3. sftp sftp@globus.si.edu
4.  password sftp123!
5. go to directory with target files
6. mget KK_GMK/*

#will copy files from sftp to server pwd
mget KK_GMK/guaricaM3428.trim_m.2.fq.gz

sftp> ! #to log out
```





## Read depth stats across WG

https://unix.stackexchange.com/questions/13731/is-there-a-way-to-get-the-min-max-median-and-average-of-a-list-of-numbers-in

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




```
# to submit to butterfly must be .sh
#!/bin/bash
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
```



## To download all files from website with password access

```

wget ‐‐http-user=popgen17 ‐‐http-password=popgen17 -r http://randy.popgen.dk/popgen17/pass/material/

wget ‐‐http-user=popgen17 ‐‐http-password=popgen17 ‐‐mirror  ‐‐accept=pdf http://randy.popgen.dk/popgen17/pass/material/

```












