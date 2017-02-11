import csv
from random import * 

with open('data_places.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)

def get_place(result):
    
    if result == "Activity":
        index = 1        
    elif result == "City Feels":    
        index = 2
    elif result == "Entertainment":
        index = 3
    elif result == "Food":
        index = 4
    elif result == "Nature":
        index = 5
    elif result == "Religious":
        index = 6
    elif result == "Shopping":
        index = 7
    elif result == "Views":
        index = 8

    l = (len(data[index]))
    print(l)
    n = sample(range(1, l), 3)
    a = []
    for i in range(0,3):
        a.append(data[index][n[i]])
    return a
