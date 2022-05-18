# a=["red","maroon","yellow","olive"]
# i=0
# b=[]
# while i<len(a):
#     c=[]
#     b.extend(a[i])
#     i+=1
# print(b)


a=["red","maroon","yellow","olive"]
i=0
b=[]
while i<len(a):
    newArr=[]
    j=0
    while j<len(a[i]):
        newArr.append(a[i][j])
        j+=1
    b.append(newArr)
    i+=1
print(b)