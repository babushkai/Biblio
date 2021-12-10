!apt-get install sqlite3
!sqlite3 ./DSTI_database.db

# SQLITE
import csv, sqlite3
import numpy as np

#con = sqlite3.connect(":memory:")
con = sqlite3.connect('DSTI_database.db')

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS t;") # what does it do ?
cur.execute("CREATE TABLE IF NOT EXISTS t (var1, var2);") # is it necessary ?

with open('data.csv','r') as fin: # `with` gives context to operate on the file
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['var1'], i['var2']) for i in dr]
    #dictReader is a collection of OrderedDicts, each containing a list of (key, value)
    #OrderedDict : a dictionary that remembers the order in which its contents are added.
    #We extract values corresponding to keys "var1" and "var2"  from each OrderedDict
    
cur.executemany("INSERT INTO t (var1, var2) VALUES (?, ?);", to_db)
con.commit()
con.close()