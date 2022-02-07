# Python mein hum ek loop ke andar loop bhi chala sakte hain Sochiye humare paas ek list hai jisme aur list hain jinme integers hain. Kuch aise:

# big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]

# big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
# counter1 = 0
# while counter1 < len(big_list):
#     small_list_length = len(big_list[counter1])
#     counter2 = 0
#     while counter2 < small_list_length:
#         print (big_list[counter1][counter2])
#         counter2 = counter2 + 1
#     counter1 = counter1 + 1
#     print ('-----')






# Question
# Socho aapke paas ek school ki class mein har student ke har subject ke marks hain. Jaise

marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
i = 0
while i < len(marks):
    max = 0
    j = 0
    while j < len(marks[i]):
        if marks[i][j] > max:
            max = marks[i][j]
        j+=1
    print(max)
    i+=1
