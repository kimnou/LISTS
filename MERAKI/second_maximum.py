l=[50,77,70,99,40,23,16]
i=0
m=l[0]
s=l[0]
while i<len(l):
    if l[i]>m:
        m=l[i]
    elif l[i]>s and l[i]<m:
        s=l[i]
    i+=1
print(s)
