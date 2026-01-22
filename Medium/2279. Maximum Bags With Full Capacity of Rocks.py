class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        ans = 0

        diff = [capacity[i] - rocks[i] for i in range(len(capacity))]
        diff.sort()
        r = additionalRocks
        for i in range(len(diff)):
            if diff[i] == 0:
                ans += 1
            elif r >= diff[i]:
                r -= diff[i]
                ans += 1
        return ans
