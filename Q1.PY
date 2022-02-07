# 1 se 1000 tak saare numbers print karne ka loop likho. Lekin

# Agar number 3 se divisible hai toh "nav" print karvao.

# Agar number 7 se divisible hai toh "gurukul" print karvao.

# Agar number 21 se divisible hai toh "navgurukul" print karvao.



# num=int(input("enter the number: "))
# i=0
# while i <= num:
#     if i%3==0:
#         print("nav")
#     elif i%7==0:
#         print("gurukul")
#     elif i%21==0:
#         print("navgurukul")
#     else:
#         print(i)
#     i+=1


num=int(input("enter the number: "))
i=1
while i <= num:
    if i%3==0 and i%7==0:
        print("navgurukul")
    elif i%3==0:
        print("nav")
    elif i%7==0:
        print("gurukul")
    else:
        print(i)
    i+=1
