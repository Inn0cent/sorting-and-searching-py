def insertionSort(lst):
    for j in range(1, len(lst)):
        x = lst[j]
        i = j-1
        while i >= 0 and lst[i] > x:
            lst[i+1] = lst[i]
            i -= 1
        lst[i+1] = x
    print(lst)


insertionSort([8,3,6,2,5,7,4,1])
