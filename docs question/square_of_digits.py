# a=[9119]
# i=0
# n=[]
# while i<len(a):
#     b=a[i]%10
#     c=a[i]//10
#     d=c%10
#     e=c//10
#     f=e%10
#     g=e//10
#     list=[g,f,d,b]
#     j=0
#     square=0
#     square2=[]
#     while j<len(list):
#         square=list[j]*(list[j])
#         square2.append(square)
#         j+=1
#     # print(square2)
#     i+=1
# for i in square2:
#     print(i,end="")

a=[9119]
i=0
string=[]
while i<len(a):
    b=str(a[i])
    i+=1
    j=0
    c=str(b)
    square=0
    while j<len(c):
        string.append(int(c[j]))
        square=string[j]*string[j]
        j+=1
        print(square,end="")