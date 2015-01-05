class Solution:
	def countAndSay(self, n):
		if n == 1:
			return '1'
		else:
			return self.decrypt(self.countAndSay(n-1))

	# @retrun string result
	def decrypt(self, n):
		prev_char = None
		counter = 0
		result = []
			
		for c in n:
			if prev_char is None:
				counter += 1
				prev_char = c
				continue
			if c != prev_char:
				result.append(str(counter))
				result.append(prev_char)
				# update
				prev_char = c
				counter = 1
			else:
				counter += 1
		
		result.append(str(counter))
		result.append(str(prev_char))
		return ''.join(result)

if __name__ == "__main__":
	s = Solution()
	for i in range(1,10):
		print s.countAndSay(i)
