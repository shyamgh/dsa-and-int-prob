class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if (len(s) <= 1):
            return len(s)

        d = {}
        p1 = 0
        p2 = 0
        max = 0

        s2 = s[0]

        for i in range(0, len(s)):

            p1 = i
            p2 = p1+1

            while (i < len(s)) and (s[i] not in s[p1:i]):
                i += 1

            if s[p1:i] not in d:
                d[s[p1:i]] = len(s[p1:i])

        for k, v in d.items():
            if v > max:
                max = v

        return max
