def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_so_far = nums[0]
    index = 1 
    arr_length = len(nums)
    init_length = len(nums)
    count_duplicate = 0
    while index < arr_length:
        if nums[index] == max_so_far:
            nums.pop(index)
            arr_length = arr_length - 1
            count_duplicate = count_duplicate + 1
        else:
            max_so_far = nums[index]
            index = index + 1
    return init_length - count_duplicate
    
# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def removeDuplicates_v2(nums):
    """
    Remove duplicates such that each unique element appears at most twice.
    :type nums: List[int]
    :rtype: int
    """
    
    index = 1     # Start with the second element in the array
    arr_length = len(nums)  # Get the length of the array
    num_curr_duplicate = 1  # Number of current duplicates
    curr_num = nums[0]    # Current number
    
    while index < arr_length:
        if(nums[index] == curr_num):
            num_curr_duplicate = num_curr_duplicate + 1
            if num_curr_duplicate > 2:
                nums.pop(index)
                arr_length = arr_length - 1
            else:
                index = index + 1

        else:
            num_curr_duplicate = 1
            curr_num = nums[index]
            index = index + 1

    return len(nums)
            