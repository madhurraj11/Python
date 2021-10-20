num = int(input("Enter number:"))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp%10
    sum += digit**order
    temp //= 10
if num == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# # Find armstrong number
# for num in range(100,10000):
#     order = len(str(num))
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** order
#         temp //= 10
#     if num == sum:
#         print("Armstrong Number",num)