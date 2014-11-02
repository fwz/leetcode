# https://oj.leetcode.com/problems/zigzag-conversion/

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        group = (nRows - 1) * 2
        size = len(s)
        redundant = size % group

        chs = []
        seq = self.genSeq(group)
        for i in range(len(seq)):
            for j in range( size / group ):
                for k in range(len(seq[i])):
                    chs.append(s[j*group + seq[i][k]])
            if redundant:
                for k in range(len(seq[i])):
                    if size / group *group + seq[i][k] < size:
                        chs.append(s[size / group *group + seq[i][k]])

        return ''.join(chs)

    def genSeq(self, group):
        assert(group % 2 == 0)
        a = []
        for i in range(group / 2 + 1 ):
            b = []
            b.append(i)
            if (i != 0 and i != group/2 ):
                b.append(group - i)
            a.append(b)
        return a

import unittest
class TestSequenceFunctions(unittest.TestCase):

    s = None

    def setUp(self):
        self.s = Solution()

    def testGenSeq(self):
        self.assertEqual(self.s.genSeq(2),[[0],[1]])
        self.assertEqual(self.s.genSeq(4),[[0],[1,3],[2]])
        self.assertEqual(self.s.genSeq(6),[[0],[1,5],[2,4],[3]])

    def testConvert(self):
        self.assertEqual(self.s.convert("PAYPALISHIRING", 3) ,"PAHNAPLSIIGYIR")
        self.assertEqual(self.s.convert("P", 1) ,"P")
        self.assertEqual(self.s.convert("P", 2) ,"P")
        self.assertEqual(self.s.convert("P", 3) ,"P")
        self.assertEqual(self.s.convert("", 3) ,"")
        self.assertEqual(self.s.convert("ABCDE", 1) ,"ABCDE")
        self.assertEqual(self.s.convert("ABCDE", 2) ,"ACEBD")
        self.assertEqual(self.s.convert("ABCDE", 3) ,"AEBDC")
        self.assertEqual(self.s.convert("ABCD", 3) ,"ABDC")

 
if __name__ == "__main__":
    unittest.main()
