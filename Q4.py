a=int(input("enter First the numbee: "))
b=int(input("enter Second the number: "))
c=int(input("enter Third the number: "))

if a>b and a>c:
    print(a,"Greater")
elif b>a and b>c:
    print(b,"Greater")
elif c>a and c>b:
    print(c,"Greater")
else:
    print("lesser")