import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
import seaborn as sns

irisData = pd.read_csv(r'C:\Users\telelink\Contacts\Desktop\irisDataSet.csv')
print(irisData.columns)

# To change Column names use rename
newData = irisData.rename(columns={"Sepal.Length": "SepalLength","Petal.Length": "PetalLength",
                      "Sepal.Width": "SepalWidth","Petal.Width": "PetalWidth"})
print(newData.columns)
print(newData.describe()) # To get the stats of the DataSet

# To plot PetalLength n SepalLength
plt.scatter(newData.PetalLength, newData.SepalLength, color = 'red')
plt.xlabel("PetalLength")
plt.ylabel("SepalLength")

# To plot indicating species with different colors using seaborn
sns.set_style('whitegrid')
sns.FacetGrid(newData, hue="Species", size =4 ).map(plt.scatter,"PetalLength","SepalLength").add_legend()
plt.xlabel("PetalLength")
plt.ylabel("SepalLength")
plt.show()





