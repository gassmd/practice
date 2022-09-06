import random

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = l + (r - l) // 2

            if target == nums[mid]:
                return mid

            elif target < nums[mid]:
                r = mid - 1

            else:
                l = mid + 1
        print('Not Found')
        return -1


nums1 = [-1, 0, 3, 4, 9, 12]
target = 9
test1 = Solution().search(nums1, target)
print(test1)


def randos():
    test2 = []
    for i in range(0,500):
        r1 = random.randint(-300, 300)
        if r1 not in test2:
            test2.append(r1)
    return sorted(test2)

nums2 = randos()

print(nums2)

test2 = Solution().search(nums2, target)

print(test2)
print(str(target) + " found at index " + str(test2))