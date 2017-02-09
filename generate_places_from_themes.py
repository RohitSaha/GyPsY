import csv
from random import * 

with open('data_places.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)

#result = raw_input("Enter theme: ")

def get_place(result):
    
    if result == "Activity":
        n = sample(range(1, len(data[1])), 3)
    elif result == "City Feels":
        n = sample(range(1, len(data[2])), 3)
    elif result == "Entertainment":
        n = sample(range(1, len(data[3])), 3)
    elif result == "Food":
        n = sample(range(1, len(data[4])), 3)
    elif result == "Historical":
        n = sample(range(1, len(data[5])), 3)
    elif result == "Nature":
        n = sample(range(1, len(data[6])), 3)
    elif result == "Religious":
        n = sample(range(1, len(data[7])), 3)
    elif result == "Shopping":
        n = sample(range(1, len(data[8])), 3)
    elif result == "Views":
        n = sample(range(1, len(data[9])), 3)
    
    a = []
    for i in range(0,3):
        a.append(data[1][n[i]])
    return a

#print(get_place(result))
