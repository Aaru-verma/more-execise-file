# Socho aapke paas do lists hain. Ab aapko nayi list banani hai jisme dono lists ke elements hone chaiye. Lekin yeh dhyan mein rakhna hai ki dono lists ke saare elements sirf ek-ek baar hi hone chaiye. Agar humare paas yeh do lists hain:

list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
i=0
while i < len(list1):
    if list1[i] not in list2:
        list2.append(list1[i])
    i+=1
j=0
while j<len(list2):
    k=0
    while k <len(list2)-j-1:
        if list2[k]>list2[k+1]:
            temp=list2[k]
            list2[k]=list2[k+1]
            list2[k+1]=temp
        k+=1
    j+=1
        
    # i+=1
print(list2)
