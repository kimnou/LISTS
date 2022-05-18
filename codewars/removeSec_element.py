###["Keep", "Remove", "Keep", "Remove", "Keep", ...]
###--> ["Keep", "Keep", "Keep", ...]

list=["keep","remove","keep","remove","keep"]
i=0
a=[]
while i<len(list):
    a.append(list[i])
    i+=2
print(a)