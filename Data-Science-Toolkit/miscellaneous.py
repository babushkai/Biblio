# import the modules we'll need
from IPython.display import HTML
import base64

# function that takes in a dataframe and creates a text link to  
# download it (will only work for files < 2MB or so)
def create_download_link(df, title = "Download CSV file", filename = "data.csv"):  
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode())
    payload = b64.decode()
    html = '<a download="{filename}" href="data:text/csv;base64,{payload}" target="_blank">{title}</a>'
    html = html.format(payload=payload,title=title,filename=filename)
    return HTML(html)

# FuzzyWuzzy is a library of Python which is used for string matching
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process


fuzz.ratio('geeksforgeeks', 'geeksgeeks') 
87

# Exact match 
fuzz.ratio('GeeksforGeeks', 'GeeksforGeeks')   

100
fuzz.ratio('geeks for geeks', 'Geeks For Geeks ')  
80


fuzz.partial_ratio("geeks for geeks", "geeks for geeks!") 
100
# Exclamation mark in second string,  
# but still partially words are same so score comes 100

fuzz.partial_ratio("geeks for geeks", "geeks geeks") 
64
# score is less because there is a extra  
# token in the middle middle of the strin


#Winden the display as default
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


def reverse_number(n):
    rev = 0
    
    while(n > 0): 
        a = n % 10
        rev = rev * 10 + a 
        n = n // 10      
    print(rev) 



