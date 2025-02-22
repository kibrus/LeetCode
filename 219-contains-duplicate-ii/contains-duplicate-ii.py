class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashtable = {}
        for i, num in enumerate(nums):
            if num in hashtable:
                if abs(hashtable[num]-i) <= k:
                    return True
            hashtable[num] = i
        return False

        