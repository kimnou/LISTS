# list=[1,2,3,4]
# i=-1
# while i>=-len(list):
#     print(list[i])
#     i-=1

list=[1,2,3,4]
i=1
reverse=[]
while i<=len(list):
    reverse.append(list[-i])
    i+=1
print(reverse)