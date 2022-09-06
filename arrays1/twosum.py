class Solution:
    def twoSumBrute(self, nums: list[int], target: int) -> list[int]:        #Brute force solution, time O(n^2), Space O(1)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):                               # loop through every element and find if another value that equals target-x
                if nums[j] == target - nums[i]:
                    return [i, j]


    def twoSum2Pass(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}                                                        # two-pass hash table, time O(n), space O(n)
        for i in range(len(nums)):
            hashmap[nums[i]] = i                                            # adds each number to hash table with value as key, index as value (k, v):(nums[i], i)
        for i in range(len(nums)):
            complement = target - nums[i]                                   # check if elements complement (target-nums[i]) exists in table, if it does return current element index and complement index
            if complement in hashmap and hashmap[complement] != i:          #complement must not be nums[i] itself
                return [i, hashmap[complement]]

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}                                                        # one-pass hash table, time O(n), space O(n)
        for i in range(len(nums)):
            complement = target - nums[i]                                   # while inserting elements into hashtable, look back and check if current elements complement already exists and return indices if it does
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


test_list1= [2,7,11,15]
test_list2= [3, 2, 4]
test1 = Solution().twoSum(test_list1, target= 9)
test2 = Solution().twoSum(test_list2, target= 6)

print(test1)
print(test2)