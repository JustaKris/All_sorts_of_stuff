import os
import pandas as pd

# Setting up input/output paths
cwd = os.path.abspath('') 
inputDir = cwd + '\Raw Files'
outputDir = cwd + '\Output'

os.chdir(inputDir)

files = os.listdir() 

# Isolating XLSX files
xlsxList = []
for file in files:
	if file.endswith('.XLSX'):
		xlsxList.append(file)		
        
# Combining all files into a single dataframe
df = pd.DataFrame()
df = df.append(pd.read_excel(str(xlsxList[0])), ignore_index=True)  # First file uset to mimic format
#df = df.append(pd.read_excel(xlsxList[0], header=17), ignore_index=False)   # This row can be used to eliminate the first semi-blank rows
for file in xlsxList[1::]:
	df = df.append(pd.read_excel(file, skiprows=range(1,19)), ignore_index=True) 
 
# Writing new file to output path
os.chdir(outputDir)
df.to_excel('Combined_StarTrack_xlsx_files.xlsx', index=False, header=False)

