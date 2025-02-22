class Solution(object):
    def containsDuplicate(self, nums):
        hashtable = {}
        for i, num in enumerate(nums):
          if num in hashtable:
            return True
          hashtable[num] = i
        return False