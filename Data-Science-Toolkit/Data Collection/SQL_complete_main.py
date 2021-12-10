# How to execute this program:
# 1. Navigate to the directory where the program folder "SQL_PythonProject_ShutimaP" is located 
# 2. In the file "GetAllSurveyData.py", in the init section of SQLDatabase class,
# please modify the values for the following variables according to your system:
# DRIVER, SERVER, DATABASE
# 3. Run the program with the command:
# >python .\myScript.py running [PATH_TO_FOLDER]\SQL_PythonProject_ShutimaP\GetAllSurveyData.py as an imported module myScript myScript.py as _main_ a_function in module

import subprocess
import sys

try:
    import pandas as pd
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pandas'])
finally:
    import pandas as pd

try:
    import pyodbc as odbc
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyodbc'])
finally:
    import pyodbc as odbc

from sql_test import SQLDatabase

def main():
    # The program will take the input of SQL view name and export CSV file name from the user
    get_view_name = input('Please, enter SQL view name (ex. vw_AllSurveyData): ')
    get_export_csv_filename = input('Please, enter the CSV file name (ex. AllSurveyData.csv): ')
    # Create an instance of the SQLDatabase class
    
    print("\n--SQL DATABASE--")
    driver_name = input('SQL Driver name? (ex. {ODBC Driver 17 for SQL Server}): ')
    server_name = input('SQL Server name? (ex. THISSIHT): ')
    database_name = input('SQL Database name? (ex. Survey_Sample_A19): ')
    mydb = SQLDatabase(get_view_name, get_export_csv_filename, driver_name, server_name, database_name)


    # Use this instance to get the list of IDs from the Survey table  
    survey_ids = mydb.get_survey_ids()
    print('Survey IDs List: ' + str(survey_ids))

    # Use this instance to get the list of IDs from the Question table
    question_ids = mydb.get_question_ids()
    print('Question IDs List: ' + str(question_ids))

    InSurveyList = mydb.CheckQuestionInSurvey(survey_ids)

    # From the query of the function above, we execute the query in SQL server, to create InSurvey data frame to be checked later
    # whether if QuestionId is InSurvey or not
    query_questionInSurvey = pd.read_sql_query(InSurveyList, mydb.sql_conn)
    df_questionInSurvey = pd.DataFrame(query_questionInSurvey)
    
    # From above SurveyId, QuestionId, InSurvey df, we take only InSurvey == 1, 
    # then convert Pandas DataFrame into a list of SurveyId and QuestionId for those with InSurvey == 1
    df_InSurvey = df_questionInSurvey.loc[df_questionInSurvey['InSurvey']==1]
    SurveyQuestion_InSurvey_List = df_InSurvey.values[:,[0,1]].tolist()

    print('Survey ID and Question ID In and NOT In Survey Structure table:')
    print(df_questionInSurvey)
    print('Survey ID and Question ID that are in Survey Structure: ' + str(SurveyQuestion_InSurvey_List))

    # Construct the SQL final query
    survey_queries_list = []
    for s in survey_ids:
        # build the query string for this survey
        question_list = []
        for q in question_ids:
            # Get the SQL for each question
            question_sql = mydb.strQueryTemplateForAnswerColumn(s, q, SurveyQuestion_InSurvey_List)
            question_list.append(question_sql)
        # Concatenate all questions SQL
        dynamic_query = ' , '.join(question_list)
        # Create the outer part of the survey query using the dynamic query
        result = mydb.strQueryTemplateOuterUnionQuery(s, dynamic_query)
        # Append to the list of queries
        survey_queries_list.append(result)
    # Join all the survey queries with UNION, strFinalQuery is the final Query to get the result All Survey Data table
    strFinalQuery = " UNION ".join(survey_queries_list)
    #print(strFinalQuery)

    #Execute the strFinalQuery in SQL to get the result All Survey Data table in order to keep it in Data Frame (for export to CSV file later)
    query_strFinalQuery = pd.read_sql_query(strFinalQuery, mydb.sql_conn)
    df_strFinalQuery = pd.DataFrame(query_strFinalQuery)
    #print(df_strFinalQuery)

    # Get the previous Survey Structure to be saved in the data frame for the comparison later
    df_savedSurveyStructure = mydb.get_survey_structure()
    #print(df_savedSurveyStructure)

    # Modified the saved Survey Structure (delete last row) and save it to test the df comparison function
    df_savedSurveyStructure2 = df_savedSurveyStructure.drop(df_savedSurveyStructure.index[3])
    #print(df_savedSurveyStructure2)

    # Get the current (new) Survey Structure to be compared with the saved one
    df_newSurveyStructure = mydb.get_survey_structure()
    #print(df_newSurveyStructure)

    # Compare the new Survey Structure tabe and the saved one, if they are different, then, activate the trigger to
    # create view in SQL management studio and create CSV file with final All Survey data table
    # else (if the new Survey Structure table is same as saved one), do nothing
    if mydb.compareSavedAndNewSurveyStructure(df_savedSurveyStructure2, df_newSurveyStructure) == True:
        print('New SurveyStructure is different from the saved one, need to trigger view')
        mydb.createViewSQL(get_view_name, strFinalQuery, mydb.sql_conn)
        mydb.createCSV(get_export_csv_filename, df_strFinalQuery)
    else:
        print('New SurveyStructure is same as saved one, do nothing')

if __name__ == '__main__':
    main()