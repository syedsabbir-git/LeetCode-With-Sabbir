class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j+=1
                nums[j],nums[i] = nums[i],nums[j]
        return j+1
        