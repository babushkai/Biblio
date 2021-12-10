import urllib.request
import os
import zipfile
import random
from shutil import copyfile

# Extract the zipfile for colab
data_url = "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip"
data_file_name = "catsdogs.zip"
download_dir = '/tmp/'
urllib.request.urlretrieve(data_url, data_file_name)
zip_ref = zipfile.ZipFile(data_file_name, 'r')
zip_ref.extractall(download_dir)
zip_ref.close()


# Second pattern
import os
from zipfile import ZipFile
path =os.getcwd()
path = "C:/Users/daisu/OneDrive/Desktop/nfnets-pytorch/hymenoptera_data.zip"
with ZipFile(path, "r") as zipd:
    zipd.extractall("/folder")
    zipd.printdir()