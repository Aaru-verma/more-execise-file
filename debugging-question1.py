# Iss program ko run karo aur dekho ki numlist aur numlistsub20 ki value same aa rahi. Iss code ko ais chane karo jisse hume num_list ki intial value bhi mil jaye.

def numbers_less_than_twenty(list):
  counter = 0
  while counter < len(list):
    item = list[counter]
    if item > 20:
      list.remove(item)
    else:
      counter += 1
  return list

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

num_list_sub_20 = numbers_less_than_twenty(num_list)

i=0
a=[]
while i <len(num_list):
  if num_list[i] not in a:
    a.append(num_list[i])
  i+=1

print ("Initial list", num_list)
print ("List that doesn't contain numbers greate than 20", num_list_sub_20)
print("num_list ki intial value",a)



