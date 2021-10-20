#Kirana Store Calculator

sum = 0
while True:
    customerinput = input("Enter the item price or Press q for quit: ")
    if customerinput != 'q':
        sum += int(customerinput)
        print(f'Your order so far: {sum}')
    else:
        print(f"Your Total Bill is {sum}. Thanks for Shopping With us!!!")
        break