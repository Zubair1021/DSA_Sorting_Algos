import random as rand
import time as tm
import csv as file


# This function generate the random array
def generate_random_array(size):
    array = [rand.randint(1, 200) for a in range(size)]  
    return array
 
#This is a Bubble Sort Fuction    
def BubbleSort(array,Start,End):
    for i in range(Start,End):
        for j in range(Start,End-i-1):
            if(array[j]>array[j+1]):
             temp=array[j]
             array[j]=array[j+1]
             array[j+1]=temp
            

    return array        
 
#main Body                
# array=generate_random_array(30000)
array=[9,8,7,6,4,3,2,1]
print("Unsorted Array",array)

Start_time =  tm.time()
array=BubbleSort(array,0,len(array))
End_time = tm.time()


print("Sorted Array",array)
print("Time Consume",End_time-Start_time)

#86.08391237258911 this is the total time consume

# this Command is used to store the Sorted array in File
with open('SortedBubbleSort.csv', 'w', newline='') as csvfile:
        writer = file.writer(csvfile)
        writer.writerows([[num] for num in array])
                                 