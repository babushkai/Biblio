import os
from pathlib import Path
import matplotlib.pyplot as plt

class Folder():
    def __init__(self, folder):
        """
        
        Attributes:
            path: input path passed as argument
            len: lengh of directory of input path
         """
            
        self.path = os.path.join(os.getcwd(), folder)
        self.len = len(os.listdir(self.path))
        self.images = list(os.listdir(self.path))
    
    def visualize(self):
        plt.figure(figsize=(12, 8))
        for index, i in enumerate(self.images):
            image = os.path.join(self.path, i)
            if self.len%2 ==0:
                x, y = int(self.len/2), int(self.len/2)
            else:
                x, y = int(self.len/2) + 1, int(self.len/2)
            plt.subplot(x, y, index + 1)
            image = plt.imread(image)
            plt.imshow(image)
            plt.title('image000{}\n'.format(index+1), fontsize = 10)
            plt.tight_layout()        
        
    def reset(self):
        self.currentDigit = 0
    
    def __iter__(self):
        self.currentDigit = 0
        return self
    
    def __next__(self):
        self.currentDigit+=1 # Initialize iteration by adding 1
        if self.currentDigit <= self.len: # Check if the current number is within a length
            image_n = "image" + str(self.currentDigit).zfill(4) + ".jpg"
            path = os.path.join(self.path, image_n)
            if Path(path).exists(): # Check if the path exists
                return path
            else:
                print("Reach the maximum length")
                raise StopIteration

    def __len__(self):
        return self.len

if __name__ == "__main__":
    dataset = Folder("images")


