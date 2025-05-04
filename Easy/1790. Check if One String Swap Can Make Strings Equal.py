class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        i = -1
        j = -1
        count = 0   # count differences!!!
        for k in range(len(s1)):
            if s1[k] != s2[k]:
                count += 1
                if i == -1: i = k
                elif j == -1: j = k
        
        if count == 0: return True
        return count == 2 and s1[i] == s2[j] and s1[j] == s2[i]

        """ my solution
        if s1 == s2: return True

        swap_idx1 = -1
        swap_idx2 = -1

        n = len(s1)
        if n == 1: return False
        for i in range(n):
            if s1[i] != s2[i]:
                swap_idx1 = i
                break
        val1 = s1[swap_idx1] # store the different value
        s1 = s1[0:swap_idx1] + s1[swap_idx1+1:] # remove the different value from the string
        val2 = s2[swap_idx1]
        s2 = s2[0:swap_idx1] + s2[swap_idx1+1:]

        for i in range(n - swap_idx1 - 1):
            if s1[i + swap_idx1] != s2[i + swap_idx1]:
                swap_idx2 = i + swap_idx1
                break
        val3 = s1[swap_idx2]
        s1 = s1[0:swap_idx2] + s1[swap_idx2+1:]
        val4 = s2[swap_idx2]
        s2 = s2[0:swap_idx2] + s2[swap_idx2+1:]

        return val1 == val4 and val2 == val3 and s1 == s2
        """
        
