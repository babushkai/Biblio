# Make a connection to database using pyodbc, then store the query in a variable then put it in pandas dataframe
# To check which ODBC Driver to use:
# 1. From Start menu, go to ODBC Data Sources
# 2. Clieck the Drivers tab, then find SQL Server ODBC Driver in the list of ODBC drivers that installed on the system

# Part 1: Stored Procedure
# Inner Loop:
# 1. Iterate in the Survey table to get all SurveyId and keep them in variable
# 2. After we get all SurveyId, this will become @currentSurveyId to be used in the loop below in step 3
#    Iterate through each Question using "currentQuestionCursor"
# 3. Check if current QuestionId is in SurveyStructure table:
#    Yes -> set InSurvey = 1
#    Then, get current QuestionId from Answer table, then update Answer 
#    string "strQueryTemplateForAnswerColumn", replace with 
#    strColumnsQueryPart AS ANS_Q(currentQuestionID)
#    No -> set InSurvey = 0
#    Then, update Answer string "strQueryTemplateForNullColumnn" to
#    NULL AS ANS_Q(currentQuestionID)
# 4. Select SurveyId, AnswerId, then update Answer string
# 5. After the last row, concatenate Answer string "strQueryTemplateForAnswerColumn" with ","
# 6. Remove the cursor "currentQuestionCursor" when finish the Inner

# Outer Loop:
# 1. Get the UserId, SurveyId and Dynamic Question Answer query from the inner loop dynamically
# 2. Union the queries together to get the final query to create All Survey data result table

def install(pandas):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pandas])

def install(pyodbc):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pyodbc])

class SQLDatabase:
    def __init__(self, view_Name, export_file_path, driver, server, database):
        self.sql_conn = odbc.connect(DRIVER=driver,
                                    SERVER=server,
                                    DATABASE=database,
                                    Trusted_Connection='yes')
        self.view_Name = view_Name
        self.export_file_path = export_file_path
    
    def _execute_query(self, query_string):
        cursor = self.sql_conn.cursor()
        cursor.execute(query_string)
        return cursor.fetchall()

    # Function to get all SurveyId from Survey table then save them in a list
    def get_survey_ids(self):
        result = self._execute_query('SELECT SurveyId FROM Survey')
        return [item[0] for item in result] 
    
    # Function to get all QuestionId from Question table then save them in a list
    def get_question_ids(self):
        result = self._execute_query('SELECT QuestionId FROM Question')
        return [item[0] for item in result]

    # Function to check whether if QuestionId is in Survey Structure table or not
    # Yes => InSurvey = 1
    # No => InSurvey = 0
    def CheckQuestionInSurvey(self, SurveyList):
        questionList = []

        for surveyId in SurveyList:
            if surveyId in range(0,len(SurveyList)):
                query_QuestionInSurvey = 'SELECT * FROM (SELECT SurveyId, QuestionId, 1 as InSurvey \
                                        FROM SurveyStructure WHERE SurveyId = ' + str(surveyId) + \
                                        ' UNION SELECT ' + str(surveyId) + ' as SurveyId, Q.QuestionId, 0 as InSurvey \
                                        FROM Question as Q WHERE NOT EXISTS ( SELECT * FROM SurveyStructure as S \
                                        WHERE S.SurveyId = ' + str(surveyId) + ' AND S.QuestionId = Q.QuestionId)) as t UNION '
                question = query_QuestionInSurvey
                questionList.append(question)
            else:
                query_QuestionInSurvey_LastRow = 'SELECT * FROM (SELECT SurveyId, QuestionId, 1 as InSurvey \
                                                FROM SurveyStructure WHERE SurveyId = ' + str(surveyId) + \
                                                ' UNION SELECT ' + str(surveyId) + ' as SurveyId, Q.QuestionId, 0 as InSurvey \
                                                FROM Question as Q WHERE NOT EXISTS ( SELECT * FROM SurveyStructure as S \
                                                WHERE S.SurveyId = ' + str(surveyId) + ' AND S.QuestionId = Q.QuestionId)) as t ORDER BY SurveyId '
                question = query_QuestionInSurvey_LastRow
                questionList.append(question)
        
            checkQuestionInSurvey = " ".join(questionList)
        surveyId += 1
        return checkQuestionInSurvey

    # Function to update the Answer
    # If SurveyId and QuestionId is InSurvey, then we get the Answer_Value from Answer table then update it in the result table dynamically 
    # along with SurveyId and QuestionId
    # If SurveyId and QuestionId is NOT InSurvey, then we update with NULL
    def strQueryTemplateForAnswerColumn(self, surveyId, questionId, allSurveyQuestionList):
        strColumnsQueryPart = ' '
    
        query_getAnswer = 'COALESCE((SELECT a.Answer_Value FROM Answer as a WHERE a.UserId = u.UserId AND a.SurveyId = ' + str(surveyId) + \
						' AND a.QuestionId = ' + str(questionId) + '), -1) AS ANS_Q' + str(questionId)
    
        query_getNoAnswer = ' NULL AS ANS_Q' + str(questionId)
    
        surveyId_questionId_pair = [surveyId, questionId]
    
        if surveyId_questionId_pair in allSurveyQuestionList:
            strColumnsQueryPart = query_getAnswer
        else:
            strColumnsQueryPart = query_getNoAnswer
    
        return strColumnsQueryPart

    # Function to do Outer loop as described above
    def strQueryTemplateOuterUnionQuery(self, surveyId, dynamicQA_list):
        finalQuery = []
    
        outerUnionQuery = 'SELECT UserId, ' + str(surveyId) + ' as SurveyId, ' + str(dynamicQA_list) + ' FROM [User] as u WHERE EXISTS(SELECT * FROM Answer as a WHERE u.UserId = a.UserId AND a.SurveyId = ' + str(surveyId) + ')'
        unionQuery = outerUnionQuery
        finalQuery.append(outerUnionQuery)
        strFinalQuery = " UNION ".join(finalQuery)
    
        return strFinalQuery

    #Part 2: Trigger
    #1. Keep the previous version of Survey Structure table in order to compared the change later
    #2. Create View in SQL and also create CSV file to keep the final table (AllSurveyData)

    # Function to SELECT data from Survey Structure table and save it to data frame
    def get_survey_structure(self):
        result = self._execute_query('SELECT * FROM SurveyStructure')
        df_previousSurveyStructure = pd.DataFrame(result)
        return df_previousSurveyStructure

    # Function to create view in SQL
    def createViewSQL(self, viewNameStr, getAllSurveyDataSQL, databaseConn):
        query_createView = ' CREATE OR ALTER VIEW ' + viewNameStr + ' AS ' + getAllSurveyDataSQL
        cursor = databaseConn.cursor()
        cursor.execute(query_createView)
        databaseConn.commit()
    
    # Function to create CSV file of All Survey data result table
    def createCSV(self, fileName, df_finalQuery):
        df_finalQuery.to_csv(fileName, index=False, header=True)
        print('Successfully export CSV file in the current directory')

    # Function to compare the current Survey Stucture data, if it's different from the saved Survey Structure, then activate the trigger
    # Else, do nothing
    def compareSavedAndNewSurveyStructure(self, savedSurveyStructure, newSurveyStructure):
        if newSurveyStructure.equals(savedSurveyStructure) == False:
            return True
        else:
            return False




