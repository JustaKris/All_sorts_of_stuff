import os
import glob
import pandas as pd

os.chdir("C:/Users/kristiyan.bonev/Desktop/Combine/Raw_Files")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, encoding='latin-1') for f in all_filenames])
#export to csv

os.chdir("C:/Users/kristiyan.bonev/Desktop/Combine")
combined_csv.to_csv( "Magick!.csv", index=False, encoding='utf-8-sig')