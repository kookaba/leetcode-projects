#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

#Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x = 0
        y = []
        for num in range(len(nums)):
            x += nums[num]
            y.append(x)
        return y