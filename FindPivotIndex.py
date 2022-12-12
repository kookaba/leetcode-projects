"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

742 / 745 testcases passed

"""
#solution four: 745 /745 testcases passed. runtime 167ms. memory 15.3 MB

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == (total - nums[i] - left_sum):
                return i
            left_sum += nums[i]
        return -1

#below are previous attempts

#solution one: 742 / 745 testcases passed
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left = nums[:i]
            right = nums[(i+1):]
            if sum(left) == sum(right):
                return i
            elif i == (len(nums)-1):
                return -1
                
                
#solution two:732 / 745 testcases passed

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lnums = len(nums)
        if lnums > 50:
            x = round(len(nums)/2)
            left_nums = (nums[:x])
            right_nums = nums[x+1:]
            if sum(left_nums) == sum(right_nums):
                return x
            elif sum(left_nums) < sum(right_nums):
                for n in range(len(right_num)):
                    if sum(nums[:n]) == sum(nums[(n+1):]):
                        return n
                    elif n == (len(right_nums)-1):
                        print("right")
                        return -1
                        
            elif sum(left_nums) > sum(right_nums):
                for n in range(len(left_nums)):
                    if sum(nums[:n]) == sum(nums[(n+1):]):
                        return n
                    elif n == (len(left_nums)-1):
                        print("left")
                        return -1
                        
        else:
            for i in range(len(nums)):
                if sum(nums[:i]) == sum(nums[(i+1):]):
                    return i
                elif i == (len(nums)-1):
                    print("neither")
                    return -1
                    
                    
#solution three: 739 / 745 testcases passed due to time limit. Passed once.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for num in range(len(nums)):
            if sum(nums[:num]) == sum(nums[(num+1):]):
                return num
            elif num == (len(nums)-1):
                return -1
                
