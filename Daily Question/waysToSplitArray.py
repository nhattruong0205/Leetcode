def waysToSplitArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    sum_value = sum(nums)
    first_half = 0
    for i in range(len(nums) - 1):
        first_half = first_half + nums[i]
        second_half = sum_value - first_half
        if first_half >= second_half:
            count = count + 1
    return count
        
        