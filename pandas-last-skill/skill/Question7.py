from math import sqrt
import sys

D=sys.argv[1].split(',')

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

