d=[]

nb=0
with open("ip.txt","r") as f:
    for s in f:
        nb+=1
    f.seek(0)
with open("ip.txt","r") as f:
    n=0  
    for s in f:
        e=s.split(";;")
        sep=','
        if n==nb-1:
            sep=''
        ss='{{"page":"{0}","ip":"{1}","date":"{2}","heure":"{3}"}}{4}'.format(e[0].strip(),e[1].strip(),e[2].strip(),e[3].strip(),sep)     
        d.append(str(ss))
        n+=1

with open("ip.json","w") as g:
    g.write("[")
    for e in d:
        g.write(e)
    g.write("]")