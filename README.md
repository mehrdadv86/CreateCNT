# CreateCNT
The script gets at CSV of stimuli from and will create a CNT region file. If each region has only one corresponding column in CSV file, it uses a simple list from parameter file. However, if there are multiple columns for one or more regions, The script will prompt questions which the user need to answer.

First thing this script is written for python 3, there are modules in it which won't work on older versions.

The script used ‘pandas’ and ‘tkinter’ packages, make sure it you have that installed before running the code. Create CNT will read in a 

CSV file containing the sentences and will output a CNT file for the regions.

If you have your sentences in an excel sheet, save it as CSV before running the code.

There are certain parameters this python code needs in order to run the program.

Number of conditions in the experiments, number of regions, the position or column of each region from the csv file. A Boolean parameter to know whether there are multiple columns for any region. 1 means there are more than one column for at least one region in the data. 0 means every region has only one single column. The final parameter is the list of the region numbers that have multiple columns. If the Boolean parameter is 0, this list is not necessary.

The parameter file will help the program run and every time you are going to run the python for an experiment you need to make sure this file is updated based on your experiment.

IMPORTANT: don't remove any of the hashtag signs in the parameter file, the only part you would need to change is the values for each parameter, based on your stimuli and experiment. Numbers related to columns are actual number not index

#running the script

After making sure the two parameters are correct, all you have to do is run the script.
Running the script will prompt two browsers, the first one will need the csv file, and the second one will need the parameter.
Names of the files are not important, but whatever name your csv file has, the CNT will have the same with a different extension. You can change the names after


If you had any problem running the script, you should contact Mehrdad Vaziri at mehrdadv@mail.usf.edu


