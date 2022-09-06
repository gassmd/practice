class Solution(object):
    def containsDuplicate(self, nums):
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i-1] == sorted_nums[i]:
                return True
        return False



    def containsDuplicateSet(self, nums):           # uses hashset, more efficient
        """
        :type nums: List[int]
        :rtype: bool
        """

        ans = set()

        for i in nums:
            if i in ans:
                return True
            ans.add(i)

        return False

print(Solution().containsDuplicate(nums = [1,2,3,4]))
print(Solution().containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))