# # New Program
#
# import threading
#
# def func1():
#     for i in range(100):
#         print("This is func1",i)
#
# def func2():
#     for i in range(100):
#         print("This is func2",i)
#
# th1 = threading.Thread(target=func1)
# th2 = threading.Thread(target=func2)
#
# th1.start()
# th2.start()

# New Program
# import threading
# def func1():
#     global x
#     for i in range(100000):
#         x+=1
#
# def func2():
#     global y
#     for i in range(100000):
#         y+=1
# x,y=0,0
# th1 = threading.Thread(target=func1)
# th2 = threading.Thread(target=func2)
#
# th1.start()
# th2.start()
#
# th1.join()
# th2.join()
# print(x,y)

# New Program

import threading

def func1():
    global x
    for i in range(1000000):
        x+=1
x=0
th1 = threading.Thread(target=func1)
th2 = threading.Thread(target=func1)

th1.start()
th2.start()
th1.join()
th2.join()
print(x)      # x is between 0 and 2000000