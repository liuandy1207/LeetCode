class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        idx = s.find("abc") # find where abc appears
        while idx != -1:   # continuously remove abc's
            s = s[:idx] + "" + s[idx+3:]
            idx = s.find("abc")
        return s == "" # if the leftover string is empty, then it was valid
