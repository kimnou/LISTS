# mainstr="the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# substr="over"
# replace="on"
# string=mainstr.split()
# i=0
# while i<len(string):
#     if substr in string:
#         string.remove(substr)
#         a=" ".join(string)
#     i+=1
# b=mainstr.replace(substr,replace)
# print(a)
# print(b)


mainstr="the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
substr="over"
replace="on"
string=mainstr.split()
i=0
while i<len(string):
    if string[i]==substr:
        del string[i]
    print(string[i],end=" ")
    i+=1
print()
a=mainstr.replace(substr,replace)
print(a)
   
