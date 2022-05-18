l=[12,45,45,17,2,4,8,10,10]
i=0
max=0
sec_max=0
a=[]
while i<len(l):
    if l[i]>max:
        max=l[i]
    elif l[i]<max and l[i]>sec_max:
        sec_max=l[i]
    i+=1
result=[max,sec_max]
print(result)
