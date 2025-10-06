class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumofztn = (n*(n+1))//2
        return sumofztn-sum(nums)