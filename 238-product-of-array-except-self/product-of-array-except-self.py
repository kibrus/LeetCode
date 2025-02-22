class Solution(object):
    def productExceptSelf(self, nums):
      output = [1]
      prefix = 1
      for i in range(len(nums)-1):
          prefix = prefix * nums[i]
          output.append(prefix)
      postfix = 1
      for i in range(len(nums)-1, 0, -1):
          postfix = postfix * nums[i]
          output[i-1] *= postfix
      return output