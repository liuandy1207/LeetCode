class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) - 1
        for i in range(n):
            print(nums[i])
            nums[i+1] += nums[i] # add the current to the next
        return nums
