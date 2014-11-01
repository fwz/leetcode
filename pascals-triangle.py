class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            result = [[1], [1,1]]
            for i in range(2, numRows):
                newRowInternal = [result[i-1][j] + result[i-1][j+1] for j in range(len(result) - 1)]
                result.append([1] + newRowInternal + [1])
            return result

if __name__ == "__main__":
    s = Solution()
    print s.generate(50)
    print s.generate(4)
    print s.generate(3)
    print s.generate(0)
