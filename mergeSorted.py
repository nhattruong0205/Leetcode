# 88 Merge Sort
def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp_arr = []  # Temporary array for merging
        index_m = 0
        index_n = 0
        
        # Only iterate over the valid parts of nums1 and nums2
        nums1_valid = nums1[:m]
        nums2_valid = nums2[:n]
        
        # Merge nums1_valid and nums2_valid into temp_arr
        while index_m < len(nums1_valid) and index_n < len(nums2_valid):
            if nums1_valid[index_m] <= nums2_valid[index_n]:
                temp_arr.append(nums1_valid[index_m])
                index_m += 1
            else:
                temp_arr.append(nums2_valid[index_n])
                index_n += 1
        
        # Add remaining elements from nums1_valid
        while index_m < len(nums1_valid):
            temp_arr.append(nums1_valid[index_m])
            index_m += 1
        
        # Add remaining elements from nums2_valid
        while index_n < len(nums2_valid):
            temp_arr.append(nums2_valid[index_n])
            index_n += 1
        
        # Modify nums1 in-place
        for i in range(len(temp_arr)):
            nums1[i] = temp_arr[i]

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.