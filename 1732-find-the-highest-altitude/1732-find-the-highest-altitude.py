class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        summ = 0
        maxx = 0
        for n in gain:
            summ+=n
            maxx=max(maxx,summ)
        return maxx
