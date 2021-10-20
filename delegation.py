# Bubble Sort
def mysort(L , key = None):
    if key == None:
        for i in range(len(L)):
            for j in range(i+1,len(L)):
                if L[i] > L[j]:
                    L[i],L[j] = L[j],L[i]
    else:
        for i in range(len(L)):
            for j in range(i+1,len(L)):
                if key(L[i]) > key(L[j]):
                    L[i],L[j] = L[j],L[i]
def inverse(e):
    return 1/e

def square(e):
    return e**2

def negative(e):
    return -e

# l1 = [21,31,12,3,2,45,34,25,41]
# mysort(l1)
# print(l1)

# l1 = [21,31,12,3,2,45,34,25,41]
# mysort(l1,key = inverse)
# print(l1)

# l1 = [21,31,-12,3,2,-45,0,34,25,41,-49,76,-77]
# mysort(l1,key = square)
# print(l1)

l1 = [21,31,-12,3,2,-45,0,34,25,41,-49,76,-77]
mysort(l1,key = negative)
print(l1)