"""
665. Non-decreasing Array

Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
"""


class Solution(object):
    def checkPossibility(self, nums):

        changed = False

        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            if changed:
                return False

            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
            changed = True
        return True


test_nums1 = [4, 2, 3]
test_nums2 = [4, 2, 1]
test1 = Solution().checkPossibility(test_nums1)
test2 = Solution().checkPossibility(test_nums2)
print(test1)
print(test2)