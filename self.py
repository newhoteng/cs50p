from functools import reduce

def maxOperations(nums, k):
    # Initialize a hash map to count occurrences of each number
    count = {}
    # Initialize operations counter
    operations = 0
    
    # Iterate through each number in the array
    for num in nums:
        # Calculate the complement
        complement = k - num
        
        # If the complement is present in the hash map and has a count greater than zero
        if complement in count and count[complement] > 0:
            # Perform an operation
            operations += 1
            # Decrease the count of the complement in the hash map
            count[complement] -= 1
        else:
            # Add the current number to the hash map or increment its count if it already exists
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
    
    # Return the total number of operations performed
    return operations
