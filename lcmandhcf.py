# # To find HCF
# def hcf(a,b):
#     if a>b:
#         smaller = b
#     else:
#         smaller = a
#     for i in range(1,smaller+1):
#         if (a%i==0 and b%i==0):
#             hcf = i
#     return hcf
#
# n1 = int(input("Enter 1st number:"))
# n2 = int(input("Enter 2nd number:"))
#
# print(f"HCF is {hcf(n1,n2)}")

# To find LCM
def lcm(a,b):
    if a>b:
        maximum = a
    else:
        maximum = b
    while (True):
        if (maximum % a == 0 and maximum % b == 0):
            lcm = maximum
            break
        maximum = maximum + 1
    return lcm

n1 = int(input("Enter 1st number:"))
n2 = int(input("Enter 2nd number:"))

print(f"LCM is {lcm(n1,n2)}")