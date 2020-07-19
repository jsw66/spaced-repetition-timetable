import pandas as pd

df = pd.read_csv(r'C:/Users/josep/Documents/test_timetable.csv')

#cuts the timetable rows and columns
df = df.iloc[0:9, 0:7]
pd.set_option("display.max_rows", None, "display.max_columns", None)

#fills in blank slots with '-' marker
df = df.fillna('-')

sessions_dict = {}
review_dict = {}
review2_dict = {}

for i in range(len(df.columns)):
    mylist = []
    list_name = df.columns[i]
    for j in range(9):
        if len(df.iat[j,i]) > 1:
            mylist.append(df.iat[j,i])
    sessions_dict[list_name] = mylist

for i in range(1, len(df.columns)):
    mylist = []
    list_name = df.columns[i]
    for j in range(9):
        if len(df.iat[j,i-1]) > 1:
            mylist.append(df.iat[j,i-1])
    review_dict[list_name] = mylist

for i in range(4, len(df.columns)):
    mylist = []
    list_name = df.columns[i]
    for j in range(9):
        if len(df.iat[j,i-4]) > 1:
            mylist.append(df.iat[j,i-4])
    review2_dict[list_name] = mylist