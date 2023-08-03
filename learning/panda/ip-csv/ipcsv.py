import pandas as pd

data=pd.read_csv("ipre.csv",sep=",",engine='python')

csv=data.drop(['rien'],axis=1)
print(set(csv['page']))
csv.to_csv("tocsv.csv",index=True)

