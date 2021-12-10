import os

cwd = os.getcwd() #'C:\\Users\\daisu\\OneDrive\\Desktop\\Toolkit\\Python'

os.listdir(cwd) 
"""['.ipynb_checkpoints',
 'argparser.py',
 'cast.py',
 'file.txt',
 'image_to_data.py',
 'module_practice',
 'os.py',
 'unit_test.py',
 '__pycache__']
"""


with open("file.txt", "r") as f:
    print(f.readlines())

os.cpu_count()
os.system

import psutil
psutil.cpu_times(True)
psutil.cpu_percent(True)

import csv
villains = [
 ['Doctor', 'No'],
 ['Rosa', 'Klebb'],
 ['Mister', 'Big'],     ['Auric', 'Goldfinger'],
 ['Ernst', 'Blofeld'],
 ]

with open('villains', 'wt') as fout:  # a context manager
    csvout = csv.writer(fout)
    csvout.writerows(villains)
    
import pandas as pd
pd.read_csv("villains")