list1=[12,3,7,78,14]
list2=[14,2,56,12,5]
i=0
a=[]
b=[]
while i<len(list1):
    if list1[i] in list2:
        a.append(list1[i])
    # else:
    #     b.append(list1[i])
    i+=1
print(a)
