import pandas as pd

a = pd.read_csv(r'C:\Users\telelink\Downloads\100SalesRecords.csv')
print(a)   # to print total data frame

print(a['Total Profit'].max()) # to get maximum profit

print(a.columns) # to get list of columns

print(a['Region'][a['Total Profit']==a['Total Profit'].max()]) # to get patricular

