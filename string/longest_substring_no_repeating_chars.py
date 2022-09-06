

class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

test_string1 = "abcabcbb"
test_string2 = "bbbbb"
test_string3 = "pwwkew"

test_result = Solution().lengthOfLongestSubstring(s = test_string3)

print(test_result)