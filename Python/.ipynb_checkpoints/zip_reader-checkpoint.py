import requests
import os 
import zipfile
import glob2

class ZipReader:
    def __init__(self, url, name, doc_type): 
        self.doc_url = url
        self.doc_name = name 
        self.doc_type = doc_type
        self.doc_path = os.path.join(os.getcwd(), self.doc_name+self.doc_type)

    def downloadFromServer(self):
        #url - location of the file
        r = requests.get(self.doc_url, stream=True)

        #save the data to a file
        if r.status_code == 200: # 200 is the successed status
            with open(self.doc_name+self.doc_type, 'wb') as f:
                f.write(r.content)
                    #check whether file exists
            if os.path.exists(self.doc_name+self.doc_type):
                print("Download is Done!")
        else:
            print("Request has failed")
            self.doc_url = input("Please, insert the correct path")
            self.downloadFromServer()

    def extractFile(self):
        with zipfile.ZipFile(self.doc_path, 'r') as zip:
            zip.printdir()
            zip.extractall(os.getcwd()+"/Zipped")

        #checking if the folder zip exists
        #assert os.path.exists() == True
        
    def remove(self):
        os.remove(self.doc_path)

    def info(self):
        print(f""" \n 
              Doc_name: {self.doc_name} \n  
              Doc_type: {self.doc_type} \n  
              Doc_url:  {self.doc_url} \n  
              Doc_path: {self.doc_path}""")


if __name__ =="__main__":
    reader = ZipReader(url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00496/QCM%20Sensor%20Alcohol%20Dataset.zip", 
                              name="alcohol", 
                              doc_type = ".zip")
    reader.downloadFromServer()
    reader.extractFile()