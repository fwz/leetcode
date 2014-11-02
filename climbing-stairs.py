# https://oj.leetcode.com/problems/climbing-stairs/

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        a = [1] * 2
        for i in range(2, n+1):
            a.append(a[i-1] + a[i-2])

        return a[n]

import unittest
class Test(unittest.TestCase):

    s = None

    def setUp(self):
        self.s = Solution()

    def test(self):
        self.assertEqual(self.s.climbStairs(0), 1)
        self.assertEqual(self.s.climbStairs(1), 1)
        self.assertEqual(self.s.climbStairs(2), 2)
        self.assertEqual(self.s.climbStairs(3), 3)

if __name__ == "__main__":
    unittest.main()
