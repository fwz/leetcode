class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        pre_sum = 0
        if root:
            return self.testCurrent(root, pre_sum, sum)
        else:
            return False

    def testCurrent(self, node, pre_sum, sum):
        if (not node.left) and (not node.right) and pre_sum + node.val == sum:
            return True

        left = False
        right = False

        if node.left:
            left = self.testCurrent(node.left, pre_sum + node.val, sum)
        if node.right:
            right = self.testCurrent(node.right, pre_sum + node.val, sum)
        return left or right


        
if __name__ == "__main__":
    n1 = TreeNode(3)
    n2 = TreeNode(4)
    n1.right = n2
    s = Solution()
    print s.hasPathSum(n1, 7)
    print s.hasPathSum(None, 7)
    print s.hasPathSum(None, 0)


