def QuickSort(A,p,r):
    if p<r:                                    # p is the first index of array
     q=partition(A,p,r)                        # q is the last index of array
     QuickSort(A,p,q-1)
     QuickSort(A,q+1,r)
    return A
    
def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
             i=i+1
             A[i],A[j] = A[j],A[i]
    A[i + 1],A[r] = A[r], A[i + 1]

    return i+1

Array=[2,6,3,5,1]
Array=QuickSort(Array,0,len(Array)-1)
print(Array)               
    