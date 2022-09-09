class Solution:
    def romanToInt(self, s: str) -> int:

        dict1 = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        num = 0
        i = 0
        while i < len(s):
            if s[i] in 'IXC' and i+1 < len(s):
                if s[i:i+2] in dict1:
                    num = num + dict1[s[i:i+2]]
                    i += 2
                else:
                    num = num + dict1[s[i]]
                    i += 1
            else:
                num = num + dict1[s[i]]
                i += 1

        return num
