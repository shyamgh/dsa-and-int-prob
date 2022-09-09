from collections import st

class Solution:
    def longestPalindrome(self, s: str) -> str:

        lpal = ''
        mx = 0

        for i in range(len(s)):

            # checking odd palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:

                if (r-l+1) > mx:
                    lpal = s[l:r+1]
                    mx = r - l + 1

                l -= 1
                r += 1

            # check even palindrome
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:

                if (r-l+1) > mx:
                    lpal = s[l:r+1]
                    mx = (r-l+1)

                l -= 1
                r += 1

        return lpal

print(Solution().longestPalindrome("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"))
