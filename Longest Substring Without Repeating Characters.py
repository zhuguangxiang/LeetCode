class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        prev_pos_dict = {}
        start = end = 0
        for i,v in enumerate(s):
            if v in prev_pos_dict:
                start = max(start,prev_pos_dict[v]+1)
            maxlen = max(maxlen, end-start+1)
            prev_pos_dict[v] = i
            end += 1
        return maxlen