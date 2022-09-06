


class Solution(object):
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



nums1 = [1, 1, 1, 2, 2, 3]
nums2 = [1]
nums3 = [1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5]

test1 = Solution().topKFrequent(nums = nums3, k = 2)

print(test1)