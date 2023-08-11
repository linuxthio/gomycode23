from math import sqrt
import sys

argv=sys.argv

if len(argv)>1:
    D=sys.argv[1].split(',')
else:
    print("Entrer une serie de nombre separee par des virgule : \n")
    D=input().split(',')


def Q(d):
    res=[]
    C=50
    H=30
    q=sqrt((2*C*d)/H)
    q=int(q)
    print(q)
        
for d in D:
    d=float(d)
    Q(d)

