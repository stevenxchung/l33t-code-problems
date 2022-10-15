'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
'''
import math
from time import time
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Find minimum k given h
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            time_to_eat = 0
            for bananas in piles:
                time_to_eat += math.ceil(bananas / k)
            if time_to_eat <= h:
                # Koko ate faster than expected, select lower values
                res = min(res, k)
                r = k - 1
            else:
                # Koko ate slower than expected, select higher values
                l = k + 1

        return res

    def reference(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = 0

        while l <= r:
            m = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += ((p - 1) // m) + 1
            if totalTime <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.minEatingSpeed(case[0], case[1]))
                else:
                    self.minEatingSpeed(case[0], case[1])
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case[0], case[1]))
                else:
                    self.reference(case[0], case[1])
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        ([3, 6, 7, 11], 8),
        ([30, 11, 23, 4, 20], 5),
        ([30, 11, 23, 4, 20], 6),
        # Additional
        ([312884470], 312884469)
    ]
    test.quantify(test_cases)