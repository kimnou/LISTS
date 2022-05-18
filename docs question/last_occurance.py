a=['s','d','f','s','d','f','s','f','k','o','p','i','w','e','k','c']
i=0
last_s=0
last_c=0
last_f=0
last_k=0
last_w=0
while i<len(a):
    if a[i]=="s":
        last_s=str(i)
    elif a[i]=="c":
        last_c=str(i)
    elif a[i]=="f":
        last_f=str(i)
    elif a[i]=="k":
        last_k=str(i)
    elif a[i]=="w":
        last_w=str(i)
    i+=1
print("last occurance of S:",last_s)
print("last occurance of C:",last_c)
print("last occurance of F:",last_f)
print("last occurance of K:",last_k)
print("last occurance of W:",last_w)