list1=['0','1','2','3','4']
list2=['red','green','black','blue','white']
list3=['100','200','300','400','500']
i=0
b=[]
while i<len(list1):
    b="".join(list1[i]+list2[i]+list3[i])
    i+=1
    print(b,end=",")