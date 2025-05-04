class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lcp = strs[0]
        lcp_len = len(lcp)

        # check one by one, not all at once!!!
        for s in strs[1:]:
            while lcp != s[0:lcp_len]:
                lcp_len -= 1
                if lcp_len == 0:
                    return ""
                lcp = lcp[0:lcp_len]
        return lcp

        """ my original solution
        lcp = ""
        for c in strs[0]:
            lcp += c
            i = 0 
            for s in strs:
                if not s:   # check empty
                    return lcp[0:len(lcp)-1]
                elif c == s[0]:
                    strs[i] = s[1:] # remove letters from the front until different
                else:
                    return lcp[0:len(lcp)-1]
                i += 1
        return lcp
        """
            
