


class Solution(object):
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res




nums1 = [2, 3, 6, 4, 6, 1]
nums2 = [6, 9, 4, 0, 2]
test1 = Solution().productExceptSelf(nums1)
test2 = Solution().productExceptSelf(nums2)
print(test1)
print(test2)