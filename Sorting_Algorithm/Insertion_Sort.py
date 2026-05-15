my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)# Traverse through 1 to len(my_array)
for i in range(1,n):# Move elements of my_array[0..i-1], that are greater than current_value, to one position ahead of their current position
    insert_index = i# Store the current value to be inserted
    current_value = my_array.pop(i)# Compare the current value with the elements in the sorted portion of the array and find the correct position to insert it
    for j in range(i-1, -1, -1):# If the current value is greater than the element at index j, update the insert index to j
        if my_array[j] > current_value:# Update the insert index to j
            insert_index = j# Insert the current value at the correct position in the sorted portion of the array
    my_array.insert(insert_index, current_value)# This code implements the insertion sort algorithm to sort an array of integers in ascending order.
  #The algorithm works by repeatedly taking the next element from the unsorted portion of the array and inserting it into the correct position in the sorted portion of the array.

print("Sorted array:", my_array)# This code will output the sorted array in ascending order.
