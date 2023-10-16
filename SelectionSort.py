import random as rand
import time as tm
import csv as file


# This function generate the random array
def generate_random_array(size):
    array = [rand.randint(1, 200) for a in range(size)]  
    return array
 
#This is a Selection Sort Fuction    
def SelectionSort(array,Start,End):
    for i in range(Start,End):
        min=i  #Initiallay we set the first element of array is smallest
        for j in range(i+1,End):
            if(array[j]<array[min]):   #If another elemnt of array is smallest than the set small element
                min=j   #Then replace our minimum element index
        temp=array[i]           #Swapping is done
        array[i]=array[min]
        array[min]=temp
            

    return array        
 
#main Body                
array=generate_random_array(10)
print("Unsorted Array",array)

Start_time =  tm.time()
array=SelectionSort(array,0,len(array))
End_time = tm.time()


print("Sorted Array",array)
print("Time Consume",End_time-Start_time)

#34.19397783279419 this is the total time consume

# this Command is used to store the Sorted array in File
with open('SortedSelectionSort.csv', 'w', newline='') as csvfile:
        writer = file.writer(csvfile)
        writer.writerows([[num] for num in array])
    
                    
            