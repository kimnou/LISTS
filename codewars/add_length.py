###add_length('apple ban') => ["apple 5", "ban 3"]
###add_length('you will win') => ["you 3", "will 4", "win 3"]

a="apple ban"
b=a.split()
c=[]
i=0
while i<len(b):
    j=0
    d=[]
    while j<len(b[i]):
        j+=1
    d.append(b[i])
    d.append(j)
    e=str(j)
    c.append(b[i]+" "+e)
    i+=1
print(c)
