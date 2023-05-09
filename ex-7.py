# Ex-7= selection sort and INSERTION

# selection
def sel(num):
    for i in range(len(num)):
        min = i
        for j in range(i + 1, len(num)):
            if num[min] > num[j]:
                min = j
        num[i], num[min] = num[min], num[i]
    print(num)


mylist = [2, 1, 7, 6, 5, 3, 4, 9, 8]
print(clist, "\n after sorting!!!!")
sel(myList)


# INSERTION
def ins(num):
    for i in range(1, len(num)):
        key = num[i]
        j = i - 1
        while j >= 0 and key < num[j]:
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = key
    print(num)


mylist = [2, 1, 7, 6, 5, 3, 4, 9, 8]
print(mylist, "\n after sorting!!!!")
ins(mylist)
