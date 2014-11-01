class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        depth = 0
        if root:
            return self.testDepth(root, depth)
        else:
            return 0

    def testDepth(self, node, depth):
        if (not node.left) and (not node.right):
            return depth + 1

        left = 0
        right = 0

        if node.left:
            left = self.testDepth(node.left, depth + 1)
        if node.right:
            right = self.testDepth(node.right, depth + 1)

        if left == 0:
            return right
        if right == 0:
            return left
        if left != 0 and right != 0:
            return min(left, right)


if __name__ == "__main__":
    s = Solution()
    n1 = TreeNode(3)
    n2 = TreeNode(4)
    n3 = TreeNode(5)
    n4 = TreeNode(5)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    print s.minDepth(n1)
    print s.minDepth(n2)
    print s.minDepth(n3)
    print s.minDepth(None)
