n = int(input("please enter the number of elements you would like the list to contain: "))
print("please enter the numbers one by one and press enter for it to be added to the list:", "\n")
l1 = []
for i in  range(n):
    l1.append(float(input()))
print("input list = ", l1)
for i in range(len(l1) - 1):
    if(l1[i] < 0):
        del l1[i]
print("output list = ", l1)