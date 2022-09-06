import collections
class Solution:

    def majorityElement1(self, nums: list[int]) -> int:         # brute force O(n^2) time, O(1) space
        majority_count = len(nums)//2                           # itereates over array, then iterates again for each numbered occurence
        for num in nums:
            count = sum(1 for elem in nums if elem == num)      # when number has appeared more than others could have, return it
            if count > majority_count:
                return num


    def majorityElement2(self, nums: list[int]) -> int:         # hashmap solution O(n) time, O(n) space

        counts = collections.Counter(nums)                      # maps elements to counter object
        return max(counts.keys(), key = counts.get)             # return element with maximum count

    def majorityElement3(self, nums: list[int]) -> int:         # sorting solution O(nlgn)

        nums.sort()
        return nums[len(nums)//2]
    


arr1 = [3,2,3]
arr2 = [2,2,1,1,1,2,2]

test1 = Solution().majorityElement1(arr1)
test2 = Solution().majorityElement1(arr2)

print(test1)
print(test2)