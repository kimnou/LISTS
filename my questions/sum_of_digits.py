# list=[12,14,35]
# i=0
# sum=0
# while i<len(list):
#     b=list[i]%10
#     c=list[i]//10
#     sum=b+c
#     print("sum of digits of",list[i],"is:",sum)
#     i+=1


list=[12,34,234,3719]
i=0
while i<len(list):
    list1=str(list[i])
    j=0
    sum=0
    while j<len(list1):
        sum=int(list1[j])+sum
        j+=1
    print(sum,end=",")
    i+=1