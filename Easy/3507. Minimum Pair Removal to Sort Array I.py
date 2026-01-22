class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        while (nums != sorted(nums)):
            min_val = nums[0] + nums[1]
            min_idx = 0
            for i in range(len(nums) - 1):
                sum_val = nums[i] + nums[i+1]
                if sum_val < min_val:
                    min_val = sum_val
                    min_idx = i
            nums.pop(min_idx)
            nums[min_idx] = min_val
            count += 1
            print(nums)
        return count
