class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0 :
            return
        step = len(nums) / k
        step_ceil = int(step) if step == int(step) else int(step) + 1
        for i in range(k):
            nums.insert(0, nums[-1])
            nums.pop()

        