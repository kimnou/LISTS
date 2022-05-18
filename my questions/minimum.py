list=[[1,2,3],[4,7,8],[6,2,3]]
i=0
s=0
a=[]
while i<len(list):
    s=min(list[i])
    a.append(s)
    i+=1
print(a)