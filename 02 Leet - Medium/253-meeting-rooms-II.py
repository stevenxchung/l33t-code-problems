'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
'''

class Solution:
    def minMeetingRooms(self, intervals):
        e = ret = 0
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        
        for s in range(len(start)):
            if start[s] < end[e]: 
                ret += 1
            else: 
                e += 1
        return ret


input = [[0, 30], [5, 10], [15, 20]]
sol = Solution()
print(sol.minMeetingRooms(input))
