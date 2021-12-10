# Objective:
#SQL
#1. to select data from tables
#2. to create/alter views

#Python
#1.Handle the connection to the database server
#2.Replicate the algorithm of the dbo.fn_GetAllSurveyDataSQL
#3.Replicate   the   algorithm   of   the   trigger dbo.trg_refreshSurveyViewfor creating/altering the view vw_AllSurveyDatawhenever applicable.
#4.For achieving (3) above, a persistence component (in any format you like: CSV, XML, JSON, etc.), storing the last known surveys’ structures should be in place. It is not acceptable  to  just  recreate  the  view  every  time: your Python  codereplacing  thetrigger behaviour must be as close as it can be, from “outside”the database.
#5.Of course, extract the “always-fresh”pivoted survey data, in a CSV file, adequately named.


# Import dependent libraries inside the script

#import pyodbc
def install(package):
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def connect_to_server():
    connectionString = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=THISSIHT;DATABASE=Survey_Sample_A19;UID=sa;PWD=249741"
    connectionString_Trusted = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=THISSIHT;DATABASE=Survey_Sample_A19;Trusted_Connection=yes"

    mssql_connection = pyodbc.connect(connectionString_Trusted)
    question = "SELECT * FROM dbo.Question"
    answer = "SELECT * FROM dbo.Answer"
    survey = "SELECT * FROM dbo.Survey"
    structure ="SELECT * FROM dbo.SurveyStructure"

    #SENDING A QUERY AND GETTING THE RESULTSET IN A PANDAS DATAFRAME
    df_question =pandas.read_sql(question, mssql_connection)
    df_answer = pandas.read_sql(answer, mssql_connection)
    df_survey = pandas.read_sql(survey, mssql_connection)
    df_structure = pandas.read_sql(structure, mssql_connection)
    print(df_question)
    print(df_answer)
    print(df_survey)
    print(df_structure)

    #### EXAMPLE - CONVERTING THE CODE OF THE STORED FUNCTION fn_GetAllSurveyDataSQL ####
    strQueryTemplateForAnswerColumn = ' \
        COALESCE( \
            ( \
                SELECT a.Answer_Value \
                FROM Answer as a \
                WHERE \
                    a.UserId = u.UserId \
                    AND a.SurveyId = <SURVEY_ID> \
                    AND a.QuestionId = <QUESTION_ID>\
            ), -1) AS ANS_Q<QUESTION_ID> '

        #### END OF EXAMPLE ####




# Example
if __name__ == '__main__':
    
    # Check if dependent libraries are installed. 
    #If installed, import all of them,
    #If not, install and import all of them
    
    import importlib
    for module in ["pandas", "pyodbc"]:
        try:
            importlib.import_module(module)
            print(f"{module} has been already installed \n")
            globals()[module] = importlib.import_module(module)
        except ModuleNotFoundError:
            print(f"{module} is not installed")
            print(f"Start installing {module}")
            install(module)
            print(f"End installing {module} \n")
            globals()[module] = importlib.import_module(module)
        else:
            continue
        
    
    # Connect to server
    try:
        connect_to_server()
    except Exception as excp:
        print("Something went wrong: " + str(excp))
        
        
