my_array = [64, 34, 25, 5, 22, 11, 90, 12] 

n = len(my_array) # Traverse through all array elements
for i in range(n-1): #Find the minimum element in remaining unsorted array
    min_index = i # Swap the found minimum element with the first element
    for j in range(i+1, n): # Compare the current element with the minimum element
        if my_array[j] < my_array[min_index]: # Update the minimum index if the current element is smaller than the minimum
            min_index = j # Remove the minimum element from its current position and insert it at the correct position
    min_value = my_array.pop(min_index) # Remove the minimum element from its current position
    my_array.insert(i, min_value) # Insert the minimum element at the correct position

print("Sorted array:", my_array) # This code implements the selection sort algorithm to sort an array of integers in ascending order. 
#The algorithm works by repeatedly selecting the minimum element from the unsorted portion of the array and moving it to the beginning of the sorted portion.
