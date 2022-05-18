list=["A",1,2,3,"B","C"]
a=[]
b=[]
i=0
while i<len(list):
    if type(list[i])==int:
        a.append(list[i])
    else:
        b.append(list[i])
    i+=1
print(a)
print(b)