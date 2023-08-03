import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("Mall_Customers.csv")

def getn(n):
    return data[:n]

def draw(p):
    plt.plot(getn(p)['CustomerID'],getn(p)['Age'],c='red')
    plt.savefig("hello.png")
    plt.show()


def getgenre(n=1):
    if n==1:
        return data[data['Gender']=='Female'].value_counts()
    return data[data['Gender']=='Male'].value_counts()

print(getgenre(20).shape,getgenre(1).shape)


# draw(90)
# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True

# print(getn(20))


