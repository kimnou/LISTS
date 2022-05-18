list=[1234, 122, 1984, 19372, 100]
i=0
last=0
while i<len(list):
    if list[i]>=10:
        last=list[i]//10
    i+=1
    print(last,end=",")