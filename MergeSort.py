import random as rand
import time as tm
import csv as file

def generate_random_array(size):
    array=[rand.randint(1, 100) for a in range(size)]
    return array


# This is a Merge Sort Algorithm

def MergeSort(array, start, end):
    if len(array)>1:  
        Left_array=[]    
        right_array=[]               
        mid = len(array)// 2
        for i in range(0,mid):
            Left_array.append(array[i])
        for j in range(mid,len(array)):
            right_array.append(array[j]) 
        MergeSort(Left_array,0,len(Left_array))
        MergeSort(right_array,0,len(right_array))
        array=Merge(array,Left_array,right_array)  
    
    return array    

# this fuction will merging the array
def Merge(array, p, q):

    i = 0    #index of Left array
    j = 0     #index of Right array
    k=0     #index of Original array
    #P for left array
    #Q for Right array

#This will do merging 
    while i < len(p) and j < len(q):
        if p[i] > q[j]:
            array[k] = p[i]
            i=i+1
        else:
            array[k] = q[j]
            j=j+1
        k=k+1
       
#Check Any Value left in left array if so then put in original array
    while i < len(p):
        array[k] = p[i]
        i=i+1
        k=k+1
#Check Any Value left in Right array if so then put in original array
    while j < len(q):
        array[k] = q[j]
        j=j+1
        k=k+1
 
    return array


#main Body

# array=generate_random_array(4)
array=[1,3,54,2,72,23,12,32,76,12]
print("Unsorted Array",array)

Start_time =  tm.time()
array=MergeSort(array,0,len(array))
End_time = tm.time()


print("Sorted Array",array)
print("Time Consume",End_time-Start_time)

# 0.33797669410705566 this is the total time consume

# this Command is used to store the Sorted array in File
with open('SortedMergeSort.csv', 'w', newline='') as csvfile:
        writer = file.writer(csvfile)
        writer.writerows([[num] for num in array])