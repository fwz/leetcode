class Solution:

    mapping = "ZABCDEFGHIJKLMNOPQRSTUVWXY"

    # @return a string
    def convertToTitle(self, num):
		res = ''
		while num > 0:
			new_char = self.mapping[num % 26]
			res = new_char + res
			if new_char != 'Z':
				num -= num % 26
			else:
				num -= 26

			num /= 26

		return res

if __name__ == "__main__":
	s = Solution()
	for i in range(1, 728):
		print str(i) + '->' + str(s.convertToTitle(i))

