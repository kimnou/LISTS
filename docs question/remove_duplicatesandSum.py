list=[1,2,3,1,2,2]
# list=[1,2,3,4,5,6,7,1,2,3,4]
i=0
a=[]
sum=0
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
        sum=sum+list[i]
    i+=1
print(a)
print(sum)
