from toolz.tests.test_dicttoolz import defaultdict


class Solution():
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list) # mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26 #one 0 for a - z
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()         # O(m * n)

strs1 = ["eat","tea","tan","ate","nat","bat"]
test1 = Solution().groupAnagrams(strs1)
print(test1)