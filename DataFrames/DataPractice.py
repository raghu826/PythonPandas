import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np


a = pd.read_csv(r'C:\Users\telelink\Downloads\100SalesRecords.csv')
# print(a)   # to print total data frame
# print(a.head())

columns = a[['Region','Unit Cost','Total Cost', 'Total Profit']]

print(columns.head())

# print(a['Total Profit'].max()) # to get maximum profit

# print(a.columns) # to get list of columns

# print(a['Region'][a['Total Profit']==a['Total Profit'].max()]) # to get particular

# print(a[:]['Region'])  # to get a particular column

columns.hist()
plt.show()
