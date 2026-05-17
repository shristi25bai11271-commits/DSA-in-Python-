def merge(left, right):# Merges two sorted lists into a single sorted list
    result = []# Initialize an empty list to hold the merged result
    i = j = 0# Initialize pointers for both lists
    
    while i < len(left) and j < len(right):# Compare elements from both lists and append the smaller one to the result
        if left[i] < right[j]:# If the current element in the left list is smaller, append it to the result and move the pointer
            result.append(left[i])# Move the pointer for the left list
            i += 1# If the current element in the right list is smaller or equal, append it to the result and move the pointer
        else:
            result.append(right[j])# Move the pointer for the right list
            j += 1# After one of the lists is exhausted, append the remaining elements of the other list to the result
            
    result.extend(left[i:])# Append any remaining elements from the left list
    result.extend(right[j:])# Append any remaining elements from the right list
    
    return result# The main function that implements the iterative merge sort algorithm

def mergeSort(arr):
    step = 1  # Starting with sub-arrays of length 1
    length = len(arr)# Continue merging until the step size exceeds the length of the array
    
    while step < length:# Merge sub-arrays in pairs
        for i in range(0, length, 2 * step):# Define the left and right sub-arrays to be merged
            left = arr[i:i + step]# Define the right sub-array, ensuring we don't go out of bounds
            right = arr[i + step:i + 2 * step]# Merge the left and right sub-arrays
            
            merged = merge(left, right)
            
            # Place the merged array back into the original array
            for j, val in enumerate(merged):
                arr[i + j] = val# Double the step size for the next iteration to merge larger sub-arrays
                
        step *= 2  # Double the sub-array length for the next iteration
        
    return arr# Example usage

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]# Call the mergeSort function and print the sorted array
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)
