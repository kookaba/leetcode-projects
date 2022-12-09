class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x = 0
        y = []
        for num in range(len(nums)):
            x += nums[num]
            y.append(x)
        return y