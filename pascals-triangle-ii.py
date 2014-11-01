class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex  == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        else:
            row = [1,1]
            for i in range(1, rowIndex):
                row = [1] + [row[j] + row[j+1] for j in range(len(row)- 1)] + [1]
            return row

if __name__ == "__main__":
    s = Solution()
    print s.getRow(5)
    print s.getRow(4)
    print s.getRow(3)
    print s.getRow(0)
    print s.getRow(1)
    print s.getRow(2)
