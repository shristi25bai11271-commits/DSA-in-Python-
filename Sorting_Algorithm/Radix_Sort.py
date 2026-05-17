def bubbleSort(arr):# Bubble Sort implementation
    n = len(arr)# Traverse through all elements in the array
    for i in range(n):# Last i elements are already in place, no need to check them
        for j in range(0, n - i - 1)# Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:# Swap arr[j] and arr[j + 1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]# Radix Sort implementation using Bubble Sort for sorting individual buckets
                
def radixSortWithBubbleSort(arr):# Find the maximum number to know the number of digits
    max_val = max(arr)# Initialize the exponent to 1 (for the least significant digit)
    exp = 1# Loop until we have processed all digits
    
    while max_val // exp > 0:# Create buckets for each digit (0-9)
        radixArray = [[],[],[],[],[],[],[],[],[],[]]# Distribute the elements into the corresponding buckets based on the current digit
        
        for num in arr:# Calculate the index for the current digit
            radixIndex = (num // exp) % 10# Append the number to the corresponding bucket
            radixArray[radixIndex].append(num)# Sort each bucket using Bubble Sort
        
        for bucket in radixArray:
            bubbleSort(bucket)# Concatenate the sorted buckets back into the original array
        
        i = 0# Update the original array with the sorted numbers from the buckets
        for bucket in radixArray:# Iterate through each bucket and place the sorted numbers back into the original array
            for num in bucket:# Place the number in the original array
                arr[i] = num# Increment the index for the original array
                i += 1# Move to the next digit
        
        exp *= 10# Move to the next digit

myArray = [170, 45, 75, 90, 802, 24, 2, 66]# Print the original array, sort it using Radix Sort with Bubble Sort, and print the sorted array
print("Original array:", myArray)
radixSortWithBubbleSort(myArray)
print("Sorted array:", myArray)
