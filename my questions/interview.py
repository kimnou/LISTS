# a='anzum'
# b=[]
# b.extend(a)
# print(b)
# i=0
# vowels=0
# consonants=0
# while i<len(b):
#     if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
#         vowels+=1
#     else:
#         consonants+=1
#     i+=1
# print("count of vowels:",vowels)
# print("count of consonants:", consonants)

# list=[1," ",2," ",4,5,6,"4"]
# i=0
# a=[]
# while i<len(list):
#     if type(list[i])==int:
#         a.append(list[i])
#     i+=1
# print(a)

# list=[1,"2",4.5,"potato",6,3.5,5.6]
# i=0
# integer=[]
# string=[]
# float=[]
# while i<len(list):
#     if type(list[i])==int:
#         integer.append(list[i])
#     elif type(list[i])==str:
#         string.append(list[i])
#     else:
#         float.append(list[i])
#     i+=1
# print(integer)
# print(string)
# print(float)

# a="hello"
# b=[]
# b.extend(a)
# i=0
# while i<len(b):
#     if b[i]=="e" or b[i]=="o":
#         c=b[i].upper()
#         print(ord(c),end="")
#     else:
#         print(b[i],end="")
#     i+=1


# a="HELLO"
# b=[]
# b.extend(a)
# i=0
# while i<len(b):
#     if b[i]=="E" or b[i]=="O":
#         # c=b[i].lower()
#         print(ord(b[i]),end="")
#     else:
#         print(b[i],end="")
#     i+=1

# a=[2,4,[7,5,[8,9]]]
# print(a[2][1])

# a=[[4],[2,[4,3],[7,8]]]
# print(a[1][0])
# print(a[1][1][1])
# print(a[1][2][0])

# a=[1,[0,1,2,[3,4,[5],6],[7,[8],9],10]]
# print(a[1][0])
# print(a[1][3][2][0])
# print(a[1][3][3])
# print(a[1][4][1][0])
# print(a[1][5])

# n=[10,11,12,13,14,17,18,19]
# sum=0
# i=0
# while i<len(n):
#     sum=sum+n[i]
#     i+=1
# print(sum)

# list=[-50,-1,-2,-12,-56]
# list.sort()
# i=0
# while i<len(list):
#     i+=1
# print(list[-2])

# l=[-50,-1,-2,-12,-56]
# i=0
# a=[]
# while i<len(l):
#     if l[i]<max(l):
#         a.append(l[i])
#         sec_max=max(a)
#     i+=1
# print(sec_max)

# =================min=====================

# n=[10,11,12,13,-9,14,17,18,19]
# i=0
# minimum=0
# while i<len(n):
#     minimum=min(n)
#     i+=1
# print(minimum)

# n=[17,12,13,14,7,19]
# i=0
# min=n[0]
# while i<len(n):
#     if n[i]<min:
#         min=n[i]
#     i+=1
# print(min)

# a=['abcd','are','always','bnyone']
# i=0
# b=[]
# while i<len(a):
#     c=[]
#     j=0
#     while j<len(a[i]):
#         c.append(a[i][j])
#         j+=1
#     b.append(c)
#     i+=1
# if b[0][0]==b[1][0]==b[2][0]==b[3][0]:
#     print("same first character")
# else:
#     print("different first character")
    
# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# b=[]
# while i<len(a):
#     print(a[i])
#     i+=1

# a=[[12,1,[],34,5,[],6,98],[],[6,7],[],[9]]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if type(a[i][j])==int:
#             b.append(a[i][j])
#         else:
#             c.append(a[i][j])
#         j+=1
#     i+=1
# print(b)

# a=[[12,1,[],34,5,[],6],[9],[],[6,7],[],[9]]
# b=[]
# i=0
# while i<len(a):
#     if type(a[i])==type([]):
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             j+=1
#     else:
#         b.append(a[i])
#     i+=1
# k=0
# while k<len(b):
#     if b[k]==[]:
#         b.remove(b[k])
#     k+=1
# print(b)

# list=[]
# i=0
# while i<1:
#     if len(list)<=0:
#         print("empty list")
#     else:
#         print("not empty list")
#     i+=1
    
# a=[1,2,3,"q","w"]
# b=a
# print(b)

# ###using builtin list() method
# a=[1,2,3,"q","w"]
# list2=list(a)
# print(list2)

# ###using copy
# a=[1,2,3,"q","w"]
# b=a.copy()
# print(b)

# a=[1,2,3,4,5]
# b=[5,6,7,8,9]
# i=0
# while i<len(a):
#     if a[i] in b:
#         print("true")
#     i+=1

# list=["red","green","white","black","pink","yellow"]
# i=0
# while i<len(list):
#     if i==0 or i==4 or i==5:
#         list.pop(i)
#     i+=1
# print(list)


# num=int(input("enter number:"))
# num2=str(num)
# print(num2[::-1])
# a=[]
# a.extend(str(num2))
# i=-1
# b=[]
# while i>=-len(a):
#     b.append(a[i])
#     c="".join(b)
#     i-=1
# print(c)



# num=int(input("enter number:"))
# num2=str(num)
# i=-1
# while i>=-len(num2):
#     print(num2[i],end="")
#     i-=1


a=[1,2,3]
b=[4,5,6]
i=0
y=[]
while i<len(a) and i<len(b):
    x=[a[i],b[i]]
    y.extend(x)
    i+=1
print(y)
    



