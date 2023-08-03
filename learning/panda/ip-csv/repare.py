dd=[]
with open("ip2.csv","r") as f:
    for c in f:
        dd.append(c)
        print(c)
        
with open("ipre.csv","w") as g:
    for e in dd:
        ed=e.split(";;")
        ss=",".join(ed)
        g.write(ss)



