def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr_length = len(nums)
        max_num = arr_length // 2
        unique_value = list(set(nums))
        for i in range(len(unique_value)):
            if nums.count(unique_value[i]) > max_num:
                return unique_value[i]
            
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2