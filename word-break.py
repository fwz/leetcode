# https://oj.leetcode.com/problems/word-break/

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1 , -1):
            for j in range(i+1, len(s)+1):
                ss = s[i:j]
                if ss in dict and dp[j]:
                    dp[i] = True
                    break

        return dp[0]


import unittest
class Test(unittest.TestCase):

    s = None

    def setUp(self):
        self.s = Solution()

    def test(self):
        self.assertEqual(self.s.wordBreak("a", set(["a"])), True)
        self.assertEqual(self.s.wordBreak("aaa", set(["a"])), True)
        self.assertEqual(self.s.wordBreak("abc", set(["a","bc"])), True)
        self.assertEqual(self.s.wordBreak("abc", set(["ac","b"])), False)
        self.assertEqual(self.s.wordBreak("leetcode", set(["leet", "code"])), True)

if __name__ == "__main__":
    unittest.main()
