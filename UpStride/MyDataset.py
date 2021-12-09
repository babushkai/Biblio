import os
from pathlib import Path

class MyDataset():
    def __init__(self, folderPath):
        """
        
        Attributes:
            path: input path passed as argument
            len: lengh of directory of input path
         """

        self.path = folderPath
        self.len = len(os.listdir(self.path))
    
    def __iter__(self):
        self.currentDigit = 0
        return self
    
    def __next__(self):
        self.currentDigit+=1 # Initialize iteration by adding 1
        if self.currentDigit <= self.len: # Check if the current number is within a length
            image_n = "/image_" + str(self.currentDigit).zfill(5) + ".jpg"
            path = self.path + image_n
            if Path(path).exists(): # Check if the path exists
                return path
            else:
                False
        else:
            print("Reach the maximum length")
            raise StopIteration

    def __len__(self):
        return self.len