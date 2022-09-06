class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        newStr = ''
        s = s.lower()

        for c in s:
            if c.isalnum():
                newStr += c

        return newStr == newStr[::-1]


    def isPalindrome1(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):                # ignore non-alphanumeric characters
                r -= 1
            if s[l].lower() != s[r].lower():                        # puts characters in lowercase and returns FALSE if they are different
                return False
            l += 1
            r -= 1
        return True

    def alphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('a') or
                ord('0') <= ord(c) <= ord('9'))

if __name__ == '__main__':
    string = 'Was it a car or a cat I saw!!'
    print(f'Is "{string}" a palindrome? : {Solution().isPalindrome1(string)}')
    string2 = 'A man, a plan,'
    print(f'Is "{string2}" a palindrome? : {Solution().isPalindrome1(string2)}')
    string3 = 'saippuakivikauppias'
    print(f'Is "{string3}" a palindrome? : {Solution().isPalindrome1(string3)}')

#left, right pointers, update left and right until each points at alphanum, compare left and right, continue until left >= right, don’t distinguish between upper/lowercase;
