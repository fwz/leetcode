# https://oj.leetcode.com/problems/maximum-product-subarray/

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        n_min = A[0]
        n_max = A[0]
        a_max = A[0]

        for i in range(1, len(A)):
            n_max, n_min = max(max(A[i], n_max*A[i]), n_min*A[i]), \
                           min(min(A[i], n_max*A[i]), n_min*A[i])

            a_max = max(a_max, n_max)

        return a_max

import unittest
class TestSequenceFunctions(unittest.TestCase):

    s = None

    def setUp(self):
        self.s = Solution()

    def test(self):
        self.assertEqual(self.s.maxProduct([-1,1,1,1,1]), 1)
        self.assertEqual(self.s.maxProduct([-1,1,-1,1,-1]), 1)
        self.assertEqual(self.s.maxProduct([-1,2,-1,2,-2]), 8)
        self.assertEqual(self.s.maxProduct([9,8,0,10,11]), 110)
        self.assertEqual(self.s.maxProduct([9,-8,0,10,-11]), 10)
        self.assertEqual(self.s.maxProduct([-1]), -1)
        self.assertEqual(self.s.maxProduct([0]), 0)
        self.assertEqual(self.s.maxProduct([2,3,-2,4]), 6)
        self.assertEqual(self.s.maxProduct([2,-3,-2,4]), 48)

if __name__ == "__main__":
    unittest.main()
