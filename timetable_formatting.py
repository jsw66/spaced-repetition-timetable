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
#counts the number of revision slots in a day
#revision_slots = []
#for n in range(7):
#    counter = 0
#    for elem in df.iloc[:, n]:
#        if elem == 'Y':
#            pass
#        elif elem == 'X':
#            pass
#        else:
#            counter += 1
#    revision_slots.append(counter)
#print(revision_slots)

##counts the number of free slots in a day
#free_slots = []
#for n in range(7):
#    counter = 0
#    for elem in df.iloc[:, n]:
#        if elem == 'Y':
#            counter += 1
#        else:
#            pass
#    free_slots.append(counter)
#print(free_slots)

    #creates initial review list for just Monday
review_list = []

for elem in df.iloc[:, 0]:
    if len(elem) > 2:
        review = elem + ' review ' + df.columns[0] 
        review_list.append(review)
        
i = 1
for j in range(15):
    if len(review_list) > 0:
        if df.iat[j, i] == 'Y':
            df.iat[j, i] = review_list[0]
            review_list.pop(0)
    else:
        pass

#creates review_list for all days apart from inital day (due to review sessions having been injected)
for i in range(1, 6):
    for elem in df.iloc[:, i]:
        if len(elem) == 1 or 'review' in elem:
            pass
        else:
            review = elem + ' review ' + df.columns[i] 
            review_list.append(review)
        p = i + 1
        for j in range(15):
            if len(review_list) > 0:
                if df.iat[j, p] == 'Y':
                    df.iat[j, p] = review_list[0]
                    review_list.pop(0)
            else:
                pass