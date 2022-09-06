

class Solution(object):
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0

        for r in range(len(s)):                     # right pointer goes to every pos in string
            count[s[r]] = 1 + count.get(s[r], 0)    # increments character count at pos r if present, 0 if it doesn't exist
            maxf = max(maxf, count[s[r]])

            while (r - 1 + 1) - maxf > k:        # while number of replacements needed ( is greater than replacements allowed (k)
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res


test_string = "ABAB"

test_result = Solution().characterReplacement(s = test_string, k = 2)
print(test_result)