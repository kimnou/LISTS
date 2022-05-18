number=30
n=[10,11,12,13,14,17,18,19]
a=[]
i=0
while i<len(n):
    j=0
    b=[]
    while j<len(n):
        if n[i]+n[j]==number:
            b.append(n[i])
            b.append(n[j])
            a.append(b)
        j+=1
    i+=1
print(a)



    