import time
start = time.time()

class Solution(object):
    def twoSumBrute(self, nums, target):            #Brute Force; time complexity O(n^2), space O(n)     
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

    def twoSumTwoPassHash(self, nums, target):      # Time complexity is O(n) from traversing list twice. Hashmap lookup is O(1). Space complexity O(n)
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

    def twoSumOnePassHash(self, nums, target):      # Time complexity O(n) from traversing list once, each lookup is O(1). Space complexity O(n)
        hashmap = {}
        print(nums)
        print(target)
        for i in range(len(nums)):
            complement = target - nums[i]
            print('comp: ' + str(complement) + ' = ' + 'targ: ' + str(target) + ' - nums[i]: ' + str(nums[i]))
            if complement in hashmap:
                print('returning ' + str(i) + '   ' + str(hashmap[complement]))
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
            print('----')
            print('nums[i]: ' + str(nums[i]))
            print('i: ' + str(i))
            print('////')
        print('00000000000000000')




print(Solution().twoSumOnePassHash(nums = [2, 7, 11, 15], target = 9))
print(Solution().twoSumOnePassHash(nums = [3, 2, 4], target= 6))
print(Solution().twoSumOnePassHash(nums = [3, 3], target = 6))
print(Solution().twoSumOnePassHash(nums = [4, 6, 3, 1, 2, 9, 13, 7], target = 12))
