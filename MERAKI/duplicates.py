# list=[1,2,3,4,1,2,3,4,5,6,7]
# i=0
# a=[]
# sum=0
# while i<len(list):
#     if list[i] not in a:
#         a.append(list[i])
#         sum=sum+a[i]
#     i+=1
# print(a)
# print(sum)

list=[1,2,3,4,1,2,3,4,5,6,7]
i=0
a=[]
sum=0
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
    i+=1
print(a)
i=0
while i<len(a):
    sum+=a[i]
    i+=1
print(sum)