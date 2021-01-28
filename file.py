import statistics as st
import csv

with open("Data.csv",newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

Mean = st.mean(new_data)
print("Mean:-",Mean)

Median = st.median(new_data)
print("Median:-",Median)

Mode = st.mode(new_data)
print("Mode:-",Mode)