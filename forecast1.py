import pandas as pd
from timetable_formatting import *

day1_sessions = []
day1_reviews = []

i=0
for j in range(9):
        if len(df.iloc[j,i]) > 1:
            day1_sessions.append(df.iloc[j,i])
print(day1_sessions)

for i in day1_sessions:
    day1_reviews.append(str(i) + ' review')
print(day1_reviews)

#def first_review():
#    for i in day1_reviews: