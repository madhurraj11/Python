# BLL Starts Here
class Customer:
    cus_list = []  # cus_list = [1000, 2000, 3000, 4000, ........]
    delete_cus = []

    def __init__(self):
        self.id = 0
        self.name = 0
        self.age = 0
        self.mob = 0

    def addCustomer(self):
        Customer.cus_list.append(self)

    def searchCustomer(self):
        for e in Customer.cus_list:
            if self.id == e.id:
                return e

    def updateCustomer(self):
        for e in Customer.cus_list:
            if self.id == e.id:
                e.name = self.name
                e.age = self.age
                e.mob = self.mob

    def deleteCustomer(self):
        for e in Customer.cus_list:
            if self.id == e.id:
                Customer.cus_list.remove(e)


# BLL Ends Here

# PL Starts Here

while True:

    cus = Customer()

    choice = input("""
    Press 1 to Add New Customer
    Press 2 to Search Customer
    Press 3 to Update Customer
    Press 4 to Delete Customer
    Press 5 to View All Customers
    Press 6 to Exit

    Enter Your Choice: """)

    if choice == '1':
        cus.id = int(input("Enter New Customer's ID: "))
        cus.name = input("Enter New Customer's Name: ")
        cus.age = int(input("Enter New Customer's Age: "))
        cus.mob = int(input("Enter New Customer's Mob: "))
        cus.addCustomer()
        print()
        print("Customer Added Successfully")
        print()

    elif choice == '2':
        cus.id = int(input("Enter Customer ID to search: "))
        cus1 = cus.searchCustomer()
        print()
        print("The Required Details are:")
        print()
        print(f"ID: {cus1.id}, Name: {cus1.name}, Age: {cus1.age}, Mob: {cus1.mob}")

    elif choice == '3':
        cus.id = int(input("Enter Customer ID to update Details: "))
        cus.name = input("Enter Updated Customer Name: ")
        cus.age = int(input("Enter Updated Customer Age: "))
        cus.mob = int(input("Enter Updated Customer Mob: "))
        cus.updateCustomer()
        print()


    elif choice == '4':
        cus.id = int(input("Enter Customer ID to delete Details: "))
        cus.deleteCustomer()

    elif choice == '5':
        print("The data of Customers is:")
        print()
        print("ID\t\tName\t\tAge\t\tMob\n")

        for e in Customer.cus_list:
            print(f"{e.id}\t\t{e.name}\t\t{e.age}\t\t{e.mob}\n")

    elif choice == '6':
        print("Thanks for using our CMS")
        break

    else:
        print("Incorrect Choice")

# PL Ends Here