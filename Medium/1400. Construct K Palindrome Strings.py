class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < k: return False     # eliminate easy cases
        count_odd = 0       # letters with even counts do NOT affect the result
        letters = "abcdefghijklmnopqrstuvwxyz"      # constructed this so i wouldn't have to remove duplicates in s
        for c in letters: 
            if s.count(c) % 2 != 0: count_odd += 1
        return count_odd <= k   # necessary condiction for it to be constructable





        """ time limit exceeded LOL
        if len(s) < k: return False

        # letters with even counts dont affect the result
        # need to consider the letters with odd counts
        count_odd = 0
        for c in s:
            if s.count(c) % 2 != 0: 
                count_odd += 1
                while s.find(c) != -1:
                    s = s[:s.find(c)] + s[s.find(c)+1:]
        return count_odd <= k
        """
          
