def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    index = 0
    n = len(nums)
    if n == 0 or k ==0:
        return
    else:
        k = k % n
    
    # Step 1: Reverse the entire array
    nums.reverse()
    
    # Step 2: Reverse the first k elements
    nums[:k] = reversed(nums[:k])
    
    # Step 3: Reverse the last n-k elements
    nums[k:] = reversed(nums[k:])


# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 
 
 # Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Reverse the whole array [1,2,3,4,5,6,7]
#                         [7,6,5,4,3,2,1]

# Reverse the first k elements (k = 3) which is [7,6,5] the one will be moved
# [5,6,7]

# Reverse the last n-k elements (n = 7, k = 3) which is [4,3,2,1] so that the original order remains
# [1,2,3,4]

# The whole new array is: [5,6,7,1,2,3,4]



# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

