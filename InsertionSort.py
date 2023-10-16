import random as rand
import time as tm
import csv as file


# This function generate the random array
def generate_random_array(size):
    array = [rand.randint(1, 200) for a in range(size)]  
    return array
 
#This is a Insertion Sort Fuction    
def InsertionSort(array,Start,End):
    for i in range(Start+1,End):
        key=array[i]
        j=i-1
        while j>=Start and array[j]>key:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
    return array        
 
#main Body                
# array=generate_random_array(30000)
array=[5,43,76,2,98,23,12,32]
print(len(array))
print("Unsorted Array",array)

Start_time =  tm.time()
array=InsertionSort(array,0,len(array))
End_time = tm.time()


print("Sorted Array",array)
print("Time Consume",End_time-Start_time)

#40.62059807777405 this is the total time consume

# this Command is used to store the Sorted array in File
with open('SortedInsertionSort.csv', 'w', newline='') as csvfile:
        writer = file.writer(csvfile)
        writer.writerows([[num] for num in array])


                

               
    