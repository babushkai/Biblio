import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

def collect_surname():
    '''
    Scrape Wikipedia's most common surname pages and
    collect common surnames in each country.
    
    Returns:
            filtered_world_surname: list of collected surnames
    '''
    world = ["Asia", "Europe", "North_America", "Oceania", "South_America"]
    world_surname = []

    for continent in world:
        response = requests.get(
            url = "https://en.wikipedia.org/wiki/List_of_most_common_surnames_in_{}".format(continent))
        soup = BeautifulSoup(response.text, 'html.parser') 
        
        # Go and get surnames on each page
        for tbody in soup.find_all('tbody'):
            for link in tbody.find_all("a"):
                world_surname.append(link.get_text())
                
    # Remove unwanted values as many as possible
    r = re.compile("[^[]") 
    filtered_world_surname = list(filter(r.match, world_surname))
    return filtered_world_surname

def load_database(file):
    '''
    Args:
            database file with arbitry format
        
    Returns:
            df: pandas DataFrame of input database
    '''
    if file.split(".")[1] == 'csv': # csv file
        df = pd.read_csv(file)
    elif file.split(".")[1] == 'xlsx': # excel file
        df = pd.read_excel(file, index_col = 0)
    elif file.split(".")[1] == "db": # sql database file
        df = pd.read_sql(file)
    return df

def detect_bug(df):
    '''
    Returns:
            bug_dict: index and name where bug occurs
            df: cleaned database
    '''
    bug_dict = {} # key: index, value: name
    for i in df.index:
        if df.name[i] not in world_surname:
            if df.firstname[i] in world_surname:
                bug_dict.setdefault(i, df.firstname[i])
                df.name[i], df.firstname[i] = df.firstname[i], df.name[i]   
            else:             
                print(f"{df.name[i]} is not in a world surname list, no way")
        else:
            continue
    return bug_dict, df


if __name__ == "__main__":
    # Dummy database
    df = pd.DataFrame({"firstname": ["Mike", "王", "Olsen", "Dupont", "Smith"], 
                   "name":["Johnson", "Ashely", "James", "Jean", "Tom"]})
    df.to_excel("name.xlsx")
    
    world_surname = collect_surname()
    df = load_database("name.xlsx")   
    print("### Before fixed Database ###")
    print(df)
    
    # Detect bug and check database again
    bug_dict, df = detect_bug(df)     
    print("\n### After fixed Database ###")
    print(df)
    print("\n### Bug list ###")   
    print(pd.Series(bug_dict))    