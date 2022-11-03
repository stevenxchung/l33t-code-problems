'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''
from time import time


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res, most_freq_c = 0, 0, 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            most_freq_c = max(most_freq_c, count[s[r]])

            if (r - l + 1) - most_freq_c > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

    def reference(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    print(self.characterReplacement(case[0], case[1]))
                else:
                    self.characterReplacement(case[0], case[1])
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
        ('ABAB', 2),
        ('AABABBA', 1),
        # Additional
        # ('AAABAAABAAAB', 1),
        # ('BBAABBAABBAA', 2),
        # ('AAAABAAAABAA', 3),
        # ('XXYYZZXXYYZZ', 4),
        # ('AAABBCAAABBC', 5)
    ]
    test.quantify(test_cases)
