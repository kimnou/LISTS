# from collections import Counter
# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# count1=Counter(list1)
# count2=Counter(list2)
# print(list(count1-count2))

list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
i=0
a=[]
while i<len(list1):
    if list1[i] not in list2:
        a.append(list1[i])
    i+=1
print(a)
