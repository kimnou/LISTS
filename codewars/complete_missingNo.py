list=[1,3,5,6,7,8]
i=0
a=[]
b=[]
while i<list[-1]:
    if i not in list:
        a.append(i)
    i+=1
    b.append(i)
print(b)
