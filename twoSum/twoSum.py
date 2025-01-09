def twoSum(nums, target):
    # Dictionary to store the indices of the numbers    
    num_to_index = {}
    
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in num_to_index:
            # Return the indices of the two numbers
            return [num_to_index[complement], i]
        
        # Store the index of the current number in the dictionary
        num_to_index[num] = i

    return None
  
