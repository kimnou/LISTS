# list=[['g','f','g'],['i','s'],['b','e','s','t']]
# i=0
# while i<len(list):
#     list1="".join(list[i])
#     i+=1
#     print(list1)

list=[['g','f','g'],['i','s'],['b','e','s','t']]
i=0
a=[]
while i<len(list):
     a.extend(list[i])
     i+=1
     list1=''.join(a)
print(list1)