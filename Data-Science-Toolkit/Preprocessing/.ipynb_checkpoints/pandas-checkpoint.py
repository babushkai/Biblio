import pandas as pd 


pd.read_csv()
pd.crosstab()
pd.value_counts().to_dict
<<<<<<< HEAD

import pandas_profiling as pdp
pdp.ProfileReport(df)


#See individual values 

lst = []
for column in columns:
  column = df_categorical[column].value_counts()
  lst.append(column)
  print("{column} \n")
=======
>>>>>>> cd3dda03879bf3a61ce1675ebb4b5d098d8755d7

# Get values which are not common in both train and test dataframe
filter1=test_df["goods_name"].isin(train_df["goods_name"])
filter2=test_df["goods_genre_name"].isin(train_df["goods_genre_name"])
filter3=test_df["store_name"].isin(train_df["store_name"])

# Filter for which are False
goods_diff = test_df.goods_name[~filter1]
genre_diff = test_df.goods_genre_name[~filter1]
store_diff = test_df.store_name[~filter1]

# Get distinct values
goods_diff = np.unique(goods_diff)
genre_diff = np.unique(genre_diff)
store_diff = np.unique(store_diff)