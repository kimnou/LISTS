### write a program that tells you how many elements are there
### in a given list.(without using len()function.)

# numbers=[50,40,23,70,56,12,5,10,7]
# print(len(numbers))

# numbers=[50,40,23,70,56,12,5,10,7]
# element=0  
# for i in numbers:
#     element+=1
# print(element)

numbers=[50,40,23,70,56,12,5,10,7]
i=0
while i<len(numbers):
    i+=1
print(i)