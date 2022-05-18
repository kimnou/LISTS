# num=int(input("enter number:"))
# i=0
# a=[]
# while i<num:
#     list=int(input("enter list:"))
#     a.append(list)
#     a.sort()
#     i+=1
# print("first_max:",max(a))
# print("second_max:",a[-2])
# print("third_max",a[-3])

list=[12,30,24,17,14]
i=0
while i<len(list):
    list.sort()
    i+=1
print("first_max:",max(list))
print("second_max",list[-2])
print("third_max:",list[-3])