# list1=[1,2,3,4,5,6]
# list2=[2,3,1,0,6,7]
# i=0
# while i<len(list1):
#     if list1[i] not in list2:
#         list2.append(list1[i])
#     if list2[i] not in list1:
#         list1.append(list2[i])
#     i+=1
# print(list1)
# print(list2)


list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
i=0
a=[]
b=[]
while i<len(list1):
    if list1[i] not in list2:
        a.append(list1[i])
    if list2[i] not in list1:
        b.append(list2[i])
    i+=1
a.append(b)
print(a)
# print(b)