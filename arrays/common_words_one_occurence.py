"""
2085. Count Common Words With One Occurrence

Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

Example 1:

Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.

Example 2:

Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
Output: 0
Explanation: There are no strings that appear in each of the two arrays.

Example 3:

Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
Output: 1
Explanation: The only string that appears exactly once in each of the two arrays is "ab".

Analysis:

    Get intersection between words1 and words2
    Find is there only one string in words1 and words2 based on step1 result.
    return string number
"""
import collections

class Solution(object):
    def countWords1(self, words1: list[str], words2: list[str]) -> int:         # O(n) time, O(n) space
        c1 = collections.Counter(words1)
        c2 = collections.Counter(words2)

        count = 0
        for x in c1.keys():
            if c1[x] == 1 and c2[x] == 1:
                count += 1
        return count

    def countWords(self, words1: list[str], words2: list[str]) -> int:


        same_w = list(set(words1) & set(words2))
        ans = 0


        for i in same_w:
            if words1.count(i) == 1 and words2.count(i) == 1:
                ans+=1
        return ans


test_words1 = ["leetcode", "is", "amazing", "as", "is"]
test_words2 = ["amazing", "leetcode", "is"]
test1 = Solution().countWords1(test_words1, test_words2)
print(test1)



