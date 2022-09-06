



class Solution(object):
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (1 + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

arr1 = [3, 4, 5, 1, 2]
arr2 = [4, 5, 6, 7, 0, 1, 2]
arr3 = [11, 13, 15, 17]

test1 = Solution().findMin(arr1)
test2 = Solution().findMin(arr2)
test3 = Solution().findMin(arr3)

print(test3)