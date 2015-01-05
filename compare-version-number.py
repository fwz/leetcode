class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]

	l1 = len(v1)
	l2 = len(v2)
	min_len = min(l1,l2)
	for i in range(min_len):
		if v1[i] < v2[i]:
			return -1
		elif v1[i] > v2[i]:
			return 1
		else:
			continue

	if l1 < l2 and sum(v2[min_len:]) > 0:
		return -1
	elif l1 > l2 and sum(v1[min_len:]) > 0:
		return 1
	else:
		return 0

if __name__ == "__main__":
	s = Solution()
	print s.compareVersion('0.1', '1.1')	
	print s.compareVersion('1.1', '1.2')	
	print s.compareVersion('1.2', '13.37')	
	print s.compareVersion('1.2', '1.2.3')	

	print s.compareVersion('1.2.3', '1.2')	

	print s.compareVersion('1.2.3', '1.2.3')	
	print s.compareVersion('1', '1')	
	print s.compareVersion('1', '1.0')	
	print s.compareVersion('1.0', '1')	
	print s.compareVersion('1.0.0', '1')	

