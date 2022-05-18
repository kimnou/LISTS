# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# elements=0
# for i in numbers:
#     elements+=1
# print(elements)

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# count=0
# while i<len(numbers):
#     if numbers[i]>=20 and numbers[i]<=40:
#         count+=1
#     i+=1
# print(count)

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# while i<len(numbers):
#     i+=1
# print(max(numbers))

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
# i=0
# while i<len(numbers):
#     numbers.sort()
#     i+=1
# print(numbers[-2])

# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# i=-1
# while i>=-len(places):
#     print(places[i])
#     i-=1

# list1=[1,2,3,4,5,6]
# list2=[2,3,1,0,6,7]
# i=0
# a=[]
# while i<len(list1):
#     if list1[i] not in list2:
#         a.append(list1[i])
#     i+=1
# print(a)

# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78],[87, 67, 49, 68, 88]]
# i=0
# sum=0
# average=0
# while i<len(marks):
#     j=0
#     sum=0
#     average=0
#     while j<len(marks[i]):
#         sum=sum+marks[i][j]
#         average=sum//len(marks[i])
#         j+=1
#     i+=1
#     print(average)

list=[1,2,3,1,2,2,4]
i=0
a=[]
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
    i+=1
print(a)

