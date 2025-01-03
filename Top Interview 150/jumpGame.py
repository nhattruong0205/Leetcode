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