class Solution:
    def reverseVowels(self, s: str) -> str:
        vset = set("aeiouAEIOU")
        s = list(s)
        l =0
        r= len(s)-1
        while l < r:
            if s[l] not in vset:
                l += 1
            elif s[r] not in vset:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)

