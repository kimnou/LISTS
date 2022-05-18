amount=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
i=0
crorepati=0
lakhpati=0
dilwale=0
while i<len(amount):
    if amount[i]>=10000000:
        crorepati+=1
    if amount[i]>=100000 and amount[i]<=10000000:
        lakhpati+=1
    if amount[i]<100000:
        dilwale+=1
    i+=1
print(crorepati,"crorepati")
print(lakhpati,"lakhpati")
print(dilwale,"dilwale")