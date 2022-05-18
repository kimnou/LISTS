list=[1234, 122, 1984, 19372, 100]
i=0
last=[]
while i<len(list):
    if list[i]>=10:
        last=list[i]%10
    i+=1
    print(last,end=",")
    
# num = 543169
# while (num >= 10):
#    num = num // 10
# print(num)