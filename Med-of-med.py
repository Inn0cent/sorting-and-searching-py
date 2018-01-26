import random
import math

def median_of_medians (A, i):
    if len(A) <= 5:
        A = sort(A)
        return A[i]
    meds = []
    slices = [A[x:x+5] for x in range(0, len(A), 5)]
    for piece in slices:
        meds.append(median_of_medians(piece, math.floor(len(piece)/2)))
    x = median_of_medians(meds, math.floor(len(piece)/2))
    x, A = Partition(A, x)
    print(A)

            
def Partition(A, x):
    i = 0
    for j in range(0, len(A)):
        if j != x and A[j] < A[x]:
            i = i+1
            A[j], A[i] = swap(A[i], A[j])
    A[x], A[i+1] = swap(A[i+1], A[x])
    return i+1, A

def sort(A):
    for i in range(0, len(A)):
        for j in range(1, len(A)):
            if A[j-1] > A[j]:
                A[j], A[j-1] = swap(A[j-1], A[j])
    return A

def swap(a,b):
    return a,b

##for i in range(10):
##    A = list(range(50000))
##    random.shuffle(A)
##    i = random.randint(0, 50000-1)
##    x = median_of_medians(A, i)
##    if x == i:
##        print('i=%d OK' % i)
##    else:
##        print('i=%d something is wrong' % i)

median_of_medians([3,6,1,3,5,7,9,4,5,8,2,6,8,4,7,6,7,8],4)
