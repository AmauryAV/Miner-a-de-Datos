#Carga de archivo
import pandas as pd
df = pd.read_csv("INM_estatal_dic25.csv")
df.head()
df.info()
df.describe()
print (df.head())