# Socho aapko paas ek list hai jisme kuch values baar baar aa rahi hain.
# Ek aisa code likho jisse aap ek nayi list banayein jisme iss list ki items ek ek baar hi aaye.



string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
a=[]
i=0
while i < len(string_list):
    if string_list[i] not in a:
        a.append(string_list[i])
    i+=1
print(a)