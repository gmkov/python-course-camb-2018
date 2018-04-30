# The read depth window challenge

This is a little scripting challenge. The result will be a useful script for checking read depth in bam files. I assume you're using python, but the same con of course be achieved with any language.

**The challenge is to write a script that computes the average read depth for windows across the genome.**

The input for the script will be the output from the `samtools depth` command. This gives the the read depth per site across all sites in the genome. This can be a huge file and it would be very difficult to visualise these data directly. We therefore want to summarise this by getting the average depth for larger windows across the genome.

## **Make the input** 

To begin, you will need a bam file, preferably with a tabix index, which will allow you to extract a smaller region for an initial test run. You can make an example input file by running samtools depth over a short region of the genome.

```
`samtools depth -r Hmel201001:1-100000 sample1.bam > sample1.depth.tsv`
```


This creates a tab-separated file in which the three columns are scaffold name, position, and read depth.

`scf1    1    7`
`scf1    2    8`
`scf1    3    8`
`scf1    4    10`
`scf1    5    12`
`scf1    6    12`


## **What should the script do?**

We want your script to read this input file and provide the **mean** and **median** read depth for windows along this scaffold. So the output should look something like:

``scaffold    start    end      mean    median
scf1        1        10000    7.2     7``
``scf1        10001    20000    13.7    12``
``scf1        20001    30000    11.9    10``

Each line also gives the scaffold, start and end position of each window. In this case the windows are 10 000 bases long.


## Tips and things to think about

### **Overlapping windows**

The windows above are non-overlapping, because each new one starts right after the previous one end. You might want the script to be able to have overlapping windows, in which the start position would be before the end position of the previous window.

### **Scaffold ends**

The example above includes only a single scaffold. The samtools depth output can contain multiple scaffolds, and transitions from one to the next would look something like this:

`scf1    93624    12`
`scf1    `93625`    13`
`scf1    `93626`    10`
`scf2    1        7`
`scf2    2        8`
`scf2    3        10`

What should the script do here? Often we don't know the correct ordering of the scaffolds in the genome, so it doesn't make sense for windows to bridge scaffold ends. Instead, you want to start a new window for the new scaffold. Like this

``scaffold    start    end       mean    median
scf1        80001    90000     7.2     7``
``scf1        90001    100000    13.7    12``
``scf2        1        10000     11.9    10``

Note that in this case the final window on scaffold 'scf1' ends at position 100 000, even though the final position on the scaffold is 93 626. You could also choose to rather include the true end position of the scaffold, but that might take a little more code.

### Use numpy

Python does not have inbuilt functions for mean and median. I use the [numpy](https://docs.scipy.org/doc/numpy/reference/routines.html) module for these. The functions `numpy.mean()` and `numpy.median()` will do what you need.

### Save space using Zipped files

One issue with this procedure is that the output from samtools depth can be a very large file if you're trying to analyse the whole genome. It will have a line for every site in the genome.

You can reduce it's size considerable by zipping it with `gzip`:


```
`samtools depth sample1.bam | gzip > sample1.depth.tsv.gz`
```

The resulting file will be a compressed file. Python can read this directly, using the [gzip](https://docs.python.org/2/library/gzip.html) module. The function `gzip.open()` works just like the generic `open()` function.

### Make it more advanced by Piping from stdin

Perhaps an even smarter way to avoid making big intermediate files is to skip that step completely. You can 'pipe' the output from samtools depth directly into your script.

The piped input is called the 'stdin'. Python can read the stdin as if it were a file. You will need to import the [sys](https://docs.python.org/2/library/sys.html) module. The object `sys.stdin` is equivalent to a file object, and you can read lines directly from there.

In the same way, you could use the sys.stdout object in place of an output file. Any lines you wruite to sys.stdout would be printed directly onto the terminal, unless you redirect them to a file. So using piping along with both sys.stdin and sys.stdout, your final result command might look like this:


```
`samtools depth sample1.bam | myDepthScript.py > sample1.depth.windows.tsv`
```


Add flexibility with command-line arguments

You might want the user to be able to modify parameters in the script from the command line. An obvious one would be the window size. You can use the [argparse](https://docs.python.org/3/library/argparse.html) module to add these. If you added a window size argument with the flag -w, your command might look like this:


```
`samtools depth sample1.bam | myDepthScript.py -w 10000 > sample1.depth.windows10kb.tsv`
```


