class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # two pointer approach has better runtime
        i = 0   # swaps the zeros
        for j in range(len(nums)):     # finds and swaps the non-zeros
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] != 0:
                i += 1

        """
        for n in nums:
            if n == 0:
                nums.remove(n)
                nums.append(n)
        """
