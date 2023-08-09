def missing_char(s,n):
    ss=""
    if n<=len(s)-1:
        for i in range(len(s)):
            if i!=n:
                ss=ss+s[i]
    return ss

print(missing_char('kitten',1))
print(missing_char('kitten',0))
print(missing_char('kitten',4))