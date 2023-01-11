'''
You are given a m x n 2D grid initialized with these three possible values.

- -1 - A wall or an obstacle. 
- 0 - A gate. 
- INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647. 

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
'''
from collections import deque
from math import inf
from time import time
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        queue = []

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            for i in range(len(queue)):
                r, c = queue.pop(0)
                for dr, dc in dir:
                    r_new = r + dr
                    c_new = c + dc
                    if (
                        r_new in range(ROWS)
                        and c_new in range(COLS)
                        and (r_new, c_new) not in visited
                        and rooms[r_new][c_new] == inf
                    ):
                        rooms[r_new][c_new] = rooms[r][c] + 1
                        queue.append((r_new, c_new))
                        visited.add((r_new, c_new))

        return rooms

    def reference(self, rooms: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def addRooms(r, c):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or rooms[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1

        return rooms

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.wallsAndGates(case))
                else:
                    self.wallsAndGates(case)
        print(f'Runtime for our solution: {time() - sol_start}\n')

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
    test_cases = [
        [
            [inf, -1, 0, inf],
            [inf, inf, inf, -1],
            [inf, -1, inf, -1],
            [0, -1, inf, inf],
        ]
    ]
    test.quantify(test_cases)
