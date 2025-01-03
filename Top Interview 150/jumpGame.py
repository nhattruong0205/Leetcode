def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    farthest = 0
    
    for i in range(len(nums)):
        # If where we start is further than our goal, we cannot jump because we only go forward, true False
        if i > farthest:
            return False

        # If where we start is not yet pass the end
        farthest = max(farthest, i + nums[i])

        # If the current place pass the end, return True
        if farthest >= len(nums) - 1:
            return True
    # If we try all the spot and still could not pass the end, return False
    return False

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

def jump(nums):
    farthest = 0
    jumps = 0
    current_end = 0
    
    for i in range(len(nums) - 1):  # No need to process the last index
        farthest = max(farthest, i + nums[i])
        
        # If we've reached the end of the current jump
        if i == current_end:
            jumps += 1
            current_end = farthest  # Move to the farthest we can reach with the current jump
            
        # If we can reach or exceed the last index
        if current_end >= len(nums) - 1:
            break
    
    return jumps

# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].