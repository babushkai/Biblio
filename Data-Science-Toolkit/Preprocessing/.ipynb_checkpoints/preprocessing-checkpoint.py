
#Replace string for None
#Use df.replace({value: None}) instead of df.replace(value, None)
#This is equivalent to s.replace(to_replace={'a': None}, value=None, method=None)
for i in range(1, 3):
    df.replace({"Missing_" + str(i): None}, inplace=True)


#One-Hot-Encoder
import pandas as pd
def oneHotEncoder(df):
  '''This Function encode input df by one-hot'''
  df_num = df.select_dtypes(exclude="object")
  df_obj = df.select_dtypes("object")
  new_df_obj = pd.get_dummies(df_obj)
  df = pd.concat([df_num, new_df_obj], axis=1)
  return df 