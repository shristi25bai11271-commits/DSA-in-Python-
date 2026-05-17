def countingSort(arr): # Counting Sort implementation
    if not arr:# Check if the input array is empty
        return arr# Find the maximum value in the array to determine the size of the count array
        
    max_val = max(arr)# Initialize the count array with zeros
    count = [0] * (max_val + 1)# Count the occurrences of each number in the input array

    for num in arr:
        count[num] += 1# Reconstruct the sorted array based on the count array
        
    arr[:] = []# Clear the original array to store the sorted elements

    for num, freq in enumerate(count):# Extend the sorted array with the current number repeated according to its frequency
        arr.extend([num] * freq) 

    return arr

unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]# Example input array
sortedArr = countingSort(unsortedArr)# Print the sorted array
print("Sorted array:", sortedArr)# Output: Sorted array: [1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6]
