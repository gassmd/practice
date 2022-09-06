"""
 495. Teemo Attacking
 https://leetcode.com/problems/teemo-attacking/
 Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds.
 More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1].
 If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.
 You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.
 Return the total number of seconds that Ashe is poisoned.
"""

class Solution(object):
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        n = len(timeSeries)
        if n == 0:
            return 0

        total = 0
        for i in range(n - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        return total + duration


times1 = [1, 4]
dur1 = 2

times2 = [1, 2]

test1 = Solution().findPoisonedDuration(timeSeries= times1, duration= dur1)
test2 = Solution().findPoisonedDuration(timeSeries= times2, duration= dur1)

print(test2)









"""
Intuition
The problem is an example of merge interval questions which are now quite popular in Google
Typically such problems could be solved in a linear time in the case of sorted input, like here, and in O(Nlog⁡N)\mathcal{O}(N \log N)O(NlogN) time otherwise, here is an example.
Here one deals with a sorted input, and the problem could be solved in one pass with a constant space. The idea is straightforward: consider only the interval between two attacks. Ashe spends in a poisoned condition the whole time interval if this interval is shorter than the poisoning time duration duration, and duration otherwise.

Algorithm
Initiate total time in poisoned condition total = 0.
Iterate over timeSeries list. At each step add to the total time the minimum between interval length and the poisoning time duration duration.
Return total + duration to take the last attack into account.
"""