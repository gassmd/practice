from collections import Counter


class Solution(object):
    def isAnagramSort(self, s: str, t: str) -> bool:        #sorting solution O(nlogn), no extra space
        return sorted(s) == sorted(t)

    def isAnagramHash(self, s:str, t: str) -> bool:     #using hashmap O(n)/O(s+t) time / O(n)/O(s+t) memory

        # return Counter(s) == Counter(t)                # 'cheating', built into python collections providing counter hashmap
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True


#hashmap to count each char in str1, decrement for str2;

print(Solution().isAnagramHash(s = "anagram", t = "nagaram"))
print(Solution().isAnagramHash(s = "car", t = "rat"))
print(Solution().isAnagramHash(s = "resistance", t = "ancestries"))
