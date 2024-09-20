def find_duplicate(nums):
    xor_result = 0
    
    # Single loop to XOR both the array elements and the range from 1 to n
    for i in range(len(nums)):
        xor_result ^= nums[i]  # XOR the array element
        if i > 0:               # Start from 1 since we need to XOR numbers from 1 to n
            xor_result ^= i     # XOR the index (which represents numbers from 1 to n)
    
    # The result is the duplicate number
    return xor_result

# Example usage
nums = [1, 3, 4, 2, 2]
print(find_duplicate(nums))  # Output: 2
