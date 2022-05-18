# list=['aba', 'xyz', 'aba', '1221']
# i=0
# count=0
# a=[]
# while i<len(list):
#     if list[i][0]==list[i][-1]:
#         a.append(list[i])
#         count+=1
#     i=i+1
# print(count)
   
# list=[1,2,3,4,5,6,7,8,9,10]
# b=[]
# i=0
# while i<len(list):
#     c=[list[i],list[i+1]]
#     b.append(c)
#     i+=2
# print(b)


# list=[]
# i=0
# while i<1:
#     if len(list)<=0:
#         print("empty list")
#     else:
#         print("not empty list")
#     i+=1

# list=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
list=[[1,4],[5,2],[7,6],[8,1]]
i=0
while i<len(list):
    j=-1
    a=[]
    while j<=len(list[i]):
        a.append([sum(list[j])])
        j+=1
    i+=1
print(a)


    