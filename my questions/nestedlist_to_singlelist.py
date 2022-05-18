# list=[[1,2,3],[4,5,6],[7],[8,9]]
# i=0
# a=[]
# while i<len(list):
#     a.extend(list[i])
#     i+=1
# print(a)

list=[1,2,3,[4,5,6],[7],[8,9]]
i=0
a=[]
while i<len(list):
    if type(list[i])==type([]):
        j=0
        while j<len(list[i]):
            a.append(list[i][j])
            j+=1
    else:
        a.append(list[i])
    i+=1
# k=0
# sum=0
# while k<len(a):
#     sum=sum+a[k]
#     k+=1
# print(sum)
print(a)






  



