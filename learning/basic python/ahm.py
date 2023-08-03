import os

ch='/home/djibril/Téléchargements/'


d=os.listdir(ch)

for e in d:
    if ".py" in e:
        print(e)