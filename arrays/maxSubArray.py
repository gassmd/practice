"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub




arr1 = [-2,1,-3,4,-1,2,1,-5,4]
arr2 = [1]
arr3 = [5, 4, -1, 7, 8]
test1 = Solution().maxSubArray(arr1)
test2 = Solution().maxSubArray(arr2)
test3 = Solution().maxSubArray(arr3)

print(test1)
print(test2)
print(test3)