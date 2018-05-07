#!/usr/bin/env python
import sys
import os
import pandas as pd

# these list the files within the current directory
# where the program is being executed
path = os.getcwd()
files = os.listdir(path)
files

# pick only .xls files, pick f is last three characters are xls
files_xls = [f for f in files if f[-3:] == 'xls']
files_xls

# Initialize empty dataframe:
df = pd.DataFrame()

# loop over list of files to append to empty dataframe:

for f in files_xls:
    data = pd.read_excel(f, skiprows=1)
    data1 = data.iloc[:,0:4].copy()
    data1['filename'] = os.path.basename(f)
    data1['sampling_cycle'] = data1['filename'].str[5:6]
    data1['datalogger_id'] = data1['filename'].str[0:4]
    #data1['sampling_cycle'] = os.path.basename(f)[1][2:]
    df = df.append(data1, ignore_index=True)
    print('I am appending to the file', f)

# now save the data frame
# index false to 

df.to_csv('output.csv', encoding='utf8', index=False)

