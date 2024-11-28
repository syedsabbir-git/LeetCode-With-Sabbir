class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        h_set = set()
        maxi = 0
        start = 0

        for end in range(len(s)):
            while s[end] in h_set:
                h_set.remove(s[start])
                start += 1
            h_set.add(s[end])
            maxi = max(maxi, end - start + 1)

        return maxi


        