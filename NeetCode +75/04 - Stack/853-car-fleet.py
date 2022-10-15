'''
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.
'''
from time import time
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Since a car cannot overtake another car, a car at front always remain car at front and car at back always remains a car at back
        arr = [(position[i], speed[i]) for i in range(len(position))]
        arr.sort(reverse=True)

        # Using stack to capture unique number of fleets
        stack = []
        for x, x_prime in arr:
            x_new = (target - x) / x_prime
            # When stack is empty or car at back is slower than car at front then it will become a new fleet
            if len(stack) == 0 or x_new > stack[-1]:
                stack.append(x_new)
           # There is no need to handle else case, if car at back is faster they become part of the fleet,
           # Hence no need to insert.

        return len(stack)

    def reference(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.carFleet(case[0], case[1], case[2]))
                else:
                    self.carFleet(case[0], case[1], case[2])
        print(f'Runtime for our solution: {time() - sol_start}')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    print(self.reference(case[0], case[1], case[2]))
                else:
                    self.reference(case[0], case[1], case[2])
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]),
        (10, [3], [3]),
        (100, [0, 2, 4], [4, 2, 1])
    ]
    test.quantify(test_cases)