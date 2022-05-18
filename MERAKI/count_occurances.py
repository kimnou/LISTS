# a=["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# i=0
# b=[]
# while i<len(a):
#     c=0
#     j=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c+=1
#         j+=1
#     if a[i] not in b:
#         b+=a[i]
#         print(a[i],c)
#     i+=1

# a="missisippy"
# i=0
# b=[]
# while i<len(a):
#     c=0
#     j=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c+=1
#         j+=1
#     if a[i] not in b:
#         b+=a[i]
#         print(a[i],c)
#     i+=1


# x="missisippy"
# i=0
# a=[]
# while i<len(x):
#     j=0
#     count=0
#     b=[]
#     while j<len(x):
#         if x[i]==x[j]:
#             count+=1
#         j+=1
#     b.append(x[i])
#     b.append(count)
#     if b not in a:
#         a.append(b)
#     i+=1
# print(a)

# # a=['m','i','s','s','i','s','i','p','y']
# a="w3school"
# i=0
# b=[]
# c=[]
# while i<len(a):
#     count=0
#     j=0
#     while j<len(a):
#         if a[i]==a[j]:
#             count+=1
#         j+=1
#     if a[i] not in b:
#         b+=a[i]
#         # print(a[i],count)
#         x=[a[i],count]
#     c.append(x)
#     i+=1
# print(c)

def count_string(a):
    i=0
    b=[]
    c=[]
    while i<len(a):
        count=0
        j=0
        while j<len(a):
            if a[i]==a[j]:
                count+=1
            j+=1
        if a[i] not in b:
            b+=a[i]
            x=[a[i],count]
        c.append(x)
        i+=1
    return c
a="w3school"
print(count_string(a))