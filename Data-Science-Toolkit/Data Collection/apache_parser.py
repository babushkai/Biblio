# Read path link, return log histories as DataFrame
def apache_line_parser(path):
    """Read log data and return DataFrame with log history"""
    import glob2
    import apache_log_parser
    import pandas as pd

    path = glob2.glob(path) # Get the path you want to parse through
    print(path)
    # Argument of make_parser is arbitrary. You get them from apache
    line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
    parsed=[]
    for path_n in path: # Go through each file in a path 
        print(path_n)
        with open(path_n) as lg:
            line_list = lg.readlines()# Read log file 
        for line in line_list: # Parse through log file and append it to parsed
            parsed.append(line_parser(line))
        
    df = pd.DataFrame(parsed) # Make DataFrame of parsed log data
    return df