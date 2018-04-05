#-------------------------------------------------------------------------------
# Name:        CreatCNT
# Purpose:     The script gets at CSV of stimuli from and will create a CNT
#              region file. If each region has only one corresponding column
#              in CSV file, it uses a simple list from parameter file.
#              However, if there are multiple columns for one or more regions,
#              The script will prompt questions which the user need to answer.
#
# Author:      Mehrdad Vaziri
# email:       mehrdadv@mail.usf.edu
#
# Created:     04/04/2018
# Copyright:   (c) Mehrdad 2018
# 
#-------------------------------------------------------------------------------
import pandas as pd
import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askinteger

Tk().withdraw()
path = askopenfilename(title = "Select Stimuli data file", filetype = (("CSV files","*.csv"),("all files","*.*")))
filename = askopenfilename(title = "Select Parameter file", filetype = (("TXT files","*.txt"),("all files","*.*")))

cnt = path[:-4]
cnt= cnt+".cnt"
path = pd.read_csv(path)
mkcnt = open(cnt,'w')
tempdf = open('tempdf', 'w+')

try:
	parameters = open(filename,'r')
	#this reads the file as text
	whole_file = parameters.read()
	#this executes the whole thing as code
	exec(whole_file)
	
except:
	print ("Your parameter file could not be found.  Or, there is an error in the file.")
	sys.exit(0)
def callback():
    newreg = e.get()
    print (newreg)

regdic = {}
if mreg ==1:
    for n in nreg:
        a={}
        b=[]
        for c in range(cond):
            newreg = askinteger("Value","Condition {0} column for region {1}?".format(c+1,n))
            a[c+1]=newreg
            regdic[n] = a

for c in range(cond):
    for index,row in path.iterrows():
        reglist = []
        reglist.append(str(row[0]))
        reglist.append(str(c+1))
        reglist.append(str(region))
        reglist.append(str(0))
        i = 0
        for a in range(region):
            if mreg ==1:
                for key in regdic.keys():
                    if a+1==key:
                        reg[key-1]=regdic.get(key)[c+1]
       
            if i==0:
                x = len(row[reg[a]-1])
                i+=1
            else:
                x = len(row[reg[a]-1])+y+1
            reglist.append(str(x))
            y = x

        re = "\t".join(reglist)
        tempdf.write(re)
        tempdf.write('\n')
        
tempdf.close()
new = pd.DataFrame(pd.read_table(tempdf.name, header=None))
new =new.sort_values([0,1]).reset_index(drop=True)

for row in new.values:
    el = []
    for i in row:
        el.append(" ")
        el.append(str(i))
    re = " ".join(el)
    mkcnt.write(re)
    mkcnt.write('\n')

mkcnt.close()
os.remove(tempdf.name)
    

    
