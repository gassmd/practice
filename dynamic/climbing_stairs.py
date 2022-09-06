class Solution(object):
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2


test_stairs = 9
test1 = Solution().climbStairs(test_stairs)

print(test1)