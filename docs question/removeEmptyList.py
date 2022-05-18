# The original list is: [5, 6, [], 3, [], [], 9]
# List after empty list removal: [5, 6, 3, 9]

# list=[5,6,[],3,[],[],9]
# i=0
# a=[]
# while i<len(list):
#     if list[i]==[]:
#         del (list[i])
#     i+=1
# print(list)

list=[5,6,[12],3,'abc',14.1,[],[],9]
i=0
a=[]
while i<len(list):
    if type(list[i])==int or type(list[i])==str or type(list[i]==float):
        a.append(list[i])
    i+=1
print(a)
