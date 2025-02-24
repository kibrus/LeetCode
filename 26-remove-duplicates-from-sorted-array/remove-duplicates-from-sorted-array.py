class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1  # First unique element is always at index 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Found a new unique element
                nums[k] = nums[i]  # Place it at the next unique position
                k += 1

        return k
        