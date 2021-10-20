n = int(input("enter the number: "))
if n>1:
    for i in range(2,n):
        if n%i == 0:
            print("Number is not Prime")
            break
    else:
        print("Number is Prime")
else:
    print("Number is not Prime")
