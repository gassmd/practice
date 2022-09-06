"""
917. Reverse Only Letters

Given a string s, reverse the string according to the following rules:

    All the characters that are not English letters remain in the same position.
    All the English letters (lowercase or uppercase) should be reversed.

Return s after reversing it.

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"

Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

"""

class Solution(object):
    def reverseOnlyLetters(self, s: str) -> str:        # stack method, O(n) time O(n) space
        letters = [c for c in s if c.isalpha()]
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)


    def reverseOnlyLetters1(self, s:str) -> str:        # reverse pointer, O(n) time O(n) space

        ans = []
        j = len(ans) - 1
        for i , x in enumerate(s):
            if x.isalpha():
                while not s[j].isalpha():
                    j -= 1
                ans.append(s[j])
                j -= 1
            else:
                ans.append(x)
        return "".join(ans)


test_str1 = "ab-cd"
test_str2 = "a-bC-dEf-ghIj"
test_str3 = "Test1ng-Leet=code-Q!"

test1 = Solution().reverseOnlyLetters(s = test_str1)
test2 = Solution().reverseOnlyLetters1(s = test_str2)
test3 = Solution().reverseOnlyLetters1(s = test_str3)

print(test1)
print(test2)
print(test3)