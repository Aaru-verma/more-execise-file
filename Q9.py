# Harshad numbers aise number hote hain jo apni digits ke sum se dhang se divide hote hain. 
# Dhang se divide hone ka matlab ki remainder 0 aata hai. Jaise 42 ek Harshad number hai kyunki 4 + 2 = 6 aur 42 ko 6 se vidie kar ke remainder aata hai

num=int(input("enter the number"))
i=num
sum=0
while  num:
    sum+=num%10
    num//=10
    if i%sum==0:
        print(i,"is harshad number")
    else:
        print(i,"is not harshad number")





# num=int(input("enter the number"))
# j = 1
# while j <= num:
#     sum=0
#     i = j
#     k=j
#     while k:
#         sum+= k%10
#         k//=10
#     if i%sum==0:
#         print(i,"is harshad number")
#     j+=1

