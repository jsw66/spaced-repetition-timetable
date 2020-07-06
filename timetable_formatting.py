import pandas as pd 
df = pd.read_csv(r'C:/Users/josep/Documents/test_timetable.csv')

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#cuts the timetable rows and columns
df = df.iloc[0:9, 0:7]
pd.set_option("display.max_rows", None, "display.max_columns", None)

#fills in blank slots with '-' marker
df = df.fillna('-')

#sorts slots into busy and free
for i in df:
    df.loc[df[i] == '*', i] = 'X'
    df.loc[df[i] == '-', i] = 'Y'
    
#colour coordinates busy and free and 'other' slots
#when connected to google calendar api, will have to change if statements to recognise event type (work/busy)
def green_and_red(val):
    if val == 'X':
        color = 'red'
        return 'color: %s' % color
    elif val == 'Y':
        color = 'green'
        return 'color: %s' % color
    else:
        color = 'blue'
        return 'color: %s' % color
    
#df = df.style.applymap(green_and_red)
print(df)