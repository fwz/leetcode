class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s == "":
            return True
        s = s.lower()
        s = ''.join( ch for ch in s if ch.isalnum())
        rs = s[::-1]
        if s == rs:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print s.isPalindrome("A man, a plan, a canal: Panama")
    print s.isPalindrome("A man")
