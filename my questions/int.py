# list=['A','B']
# n=int(input("enter number:"))
# i=1
# b=[]
# while i<=n:
#     j=0
#     while j<len(list):
#         c=list[j]+str(i)
#         b.append(c)
#         j+=1
#     i+=1
# print(b)

# a=input("enter input:")
# if "ing" not in a:
#     print(a+"ing")

# a=[2,4,6,8,4,2,9,8]
# b=[]
# c=[]
# i=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i+=1
# print(c)

# myArray1 = [0] 
# myArray2 = [1]

# while myArray2 < 700:
#     myArray1, myArray2 = b[i], myArray1+myArray2[i]
#     print(myArray2)

# a = 0
# b = 1

# while b < 700:
#     a, b = b, a+b
#     print(b)

# list=[1,2,7,9,5,6,4,12,67,98,34,14,8]
# i=0
# a=[]
# b=[]
# while i<len(list):
#     if list[i]%2==0:
#         a.append(list[i])
#     else:
#         b.append(list[i])
#     i+=1
# print(b)

# a=[1,2,3,4,5]
# b=[1,6,3,7,2]
# i=0
# j=0
# c=[]
# d=[]
# while i<len(a):
#     if a[i] not in b:
#         c.append(a[i])
#     i+=1
# print(c)
# while j<len(b):
#     if b[j] not in a:
#         d.append(b[j])
#     j+=1
# c.extend(d)
# print(d)
# print(c)

# n=[]
# for i in range(1,21):
#     n.append(i**2)
# list=n
# print (list[5:21])

# list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# i=1
# a=[]
# while i<len(list):
#     a.append(i**2)
#     i+=1
# print("square of first five:",a[:5])
# print("square of last five:",a[-5:])
# print("square of elements except first five:",a[5:])
