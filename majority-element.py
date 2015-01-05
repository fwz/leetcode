class Solution:
    # @param num, a list of integers
    # @return an integer
	# based on moore voting, num is not null
    def majorityElement(self, num):
		counter = 1
		res = num[0]
		
		for n in num[1:]:
			if counter != 0:
				if n == res: 
					counter += 1
				else:
					counter -= 1
			else:
				counter = 1
				res = n
		
		return res
        
if __name__ == "__main__":
	s = Solution()
	print s.majorityElement([1,2,3,4,1,2,3,3,3,3,3])
	print s.majorityElement([1])
	print s.majorityElement([2,2,1])
	print s.majorityElement([2,2])
