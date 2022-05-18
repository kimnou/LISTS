# num=int(input("enter number:"))
# n=[]
# for i in range(num):
#     i=int(input("enter number:"))
#     n.append(i)
# print(n)
# print("maximum is",max(n))
# print("minimum is",min(n))

# num=int(input("enter number:"))
# n=[]
# i=0
# while i<num:
#     num1=int(input("enter number"))
#     n.append(num1)
#     i+=1
# print(n)
# print(max(n),"maximum")
# print(min(n),"minimum")


num=int(input("enter required number:"))
n=[]
i=0
while i<num:
    num1=int(input("enter number:"))
    n.append(num1)
    i+=1
    j=0
    maximum=n[0]
    minimum=n[0]
    while j<len(n):
        if n[j]>maximum:
            maximum=n[j]
        if n[j]<minimum:
            minimum=n[j]
        j+=1
print("maximum is:",maximum)
print("minimum is:",minimum)
    