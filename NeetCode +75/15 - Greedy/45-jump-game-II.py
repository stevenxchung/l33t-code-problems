'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
'''
from time import time
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> bool:
        N, i, j, step = len(nums), 0, 0, 0
        while j < N - 1:
            step += 1
            max_jump = j + 1
            for i in range(i, j + 1):
                if i + nums[i] >= N - 1:
                    return step
                max_jump = max(max_jump, i + nums[i])
            i, j = j + 1, max_jump

        return step

    def reference(self, nums: List[int]) -> bool:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.jump(case))
                else:
                    self.jump(case)
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case))
                else:
                    self.reference(case)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [[2, 3, 1, 1, 4], [2, 3, 0, 1, 4]]
    test.quantify(test_cases)
