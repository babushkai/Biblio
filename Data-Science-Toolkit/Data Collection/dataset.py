import requests
import os
import glob2
import zipfile

class Dataset:
  def __init__(self, url, name, type_doc):
    self.doc_url = url
    self.doc_name = name
    self.doc_type = type_doc

  def downloadFromServer(self):
  #Get the url
    r = requests.get(self.doc_url)
    with open(self.doc_name, "wb") as f:
      f.write(r.content)
    # Check whether a loaded file exists
    assert os.path.exists(self.doc_name) == True, f"We cannot find {self.doc_name}"
  
  def extractFile(self, verbose = True):
    with zipfile.ZipFile(self.doc_name, 'r') as zip:
      zip.extractall()
      zip.printdir()

    #check if the contents of the zip file have been actually extracted
    #glob2.glob returns a list of files in a directory
    assert len(glob2.glob('*/*.csv')) > 0, f"We cannot find extracted file"
    
if __name__ == "__main__":
    url = input("What is URL?")
    
    
    