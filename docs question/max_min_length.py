list=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
count=0
a=[]
while i<len(list):
    length=len(list[i])
    a.append(length)
    i+=1
print("max_length",max(a),":",list[4])
print("min_length",min(a),":",list[1])

