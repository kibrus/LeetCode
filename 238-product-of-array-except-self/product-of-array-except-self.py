class Solution(object):
    def productExceptSelf(self, nums):
      output = [1, ]
      prefix = 1
      postfix = 1
      for i in range(len(nums)-1):
          prefix = prefix * nums[i]
          output.append(prefix)
      for i in range(len(nums)-1, 0, -1):
          print(i)
          postfix = postfix * nums[i]
          output[i-1] *= postfix
      return output