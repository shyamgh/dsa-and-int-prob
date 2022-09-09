
# def longestPalinSubstring(str):
#     # Write your code here.
#     ptr1 = 0
#     long_p = ''

#     if len(str) == 1:
#         return str

#     while ptr1 < len(str):
#         ptr2 = ptr1+1
#         while ptr2 <= len(str):
#             if str[ptr1:ptr2] == str[ptr1:ptr2][::-1]:
#                 if len(str[ptr1:ptr2]) > len(long_p):
#                     long_p = str[ptr1:ptr2]
#             ptr2 += 1
#         ptr1 += 1
#     return long_p

# LOGIC IS TO MOVE LEFT POINTER BACK AND RIGHT POINTER AHEAD TOLL

def longestPalinSubstring(str):
    # Write your code here.
    start = 0
    max = 1
    if len(str) == 1:
        return str

    for i in range(len(str)):
        lp = i-1
        rp = i+1
        # Move left pointer backward till current char and backward char are equal
        while lp >= 0 and str[lp] == str[i]:
            lp -= 1
        # Move right pointer ahead till current char and forward char are equal
        while rp < len(str) and str[rp] == str[i]:
            rp += 1
        # Move left pointer backward and right pointer ahead till backward char and forward char are equal
        while lp >= 0 and rp < len(str) and str[lp] == str[rp]:
            lp -= 1
            rp += 1

        ln = rp - lp - 1
        if(ln > max):
            max = ln
            start = lp+1

    return str[start:start+max]


'''
Problem Statement
You are given a string (STR) of length N.
Your task is to find the longest palindromic substring. If there is more than one palindromic substring with the maximum length, return the one with the smaller start index.
Note:

A substring is a contiguous segment of a string.

For example :

The longest palindromic substring of "ababc" is "aba", since "aba" is a palindrome and it is the longest substring of length 3 which is a palindrome. There is another palindromic substring of length 3 is "bab". Since starting index of "aba" is less than "bab", so "aba" is the answer.

Input Format:

The first line of input contains a single integer 'T', representing the number of test cases or queries to be run. 
Then the 'T' test cases follow.

The first and only one of each test case contains a string (STR).

Output Format :

For every test case, print a single line containing the longest palindromic substring. 

If there are multiple possible answers then you need to print the substring which has the lowest starting index.

Note :

You do not need to print anything; it has already been taken care of. Just implement the given function.

Follow up:

Try to solve it using O(1) space complexity.

Constraints :

1 <= T <= 10
0 <= N <= 10^3

where 'T' is the number of test cases, 'N' is the length of the given string.

Time Limit: 1 sec

Sample Input 1:

1
abccbc

Sample Output 1:

bccb

Explanation for input 1:

For string "abccbc" there are multiple palindromic substrings like "a", "b", "c", "cc", "bccb", "cbc". But "bccb" is of the longest length. Thus, answer is "bccb".

Sample Input 2:

1
aeiou

Sample Output 2:

a

Explanation for input 2:

For string "aeiou" there are multiple palindromic substrings like "a", "e", "I", "o", "u", and all of the same length. But palindromic substring "a"  has the minimum starting index. Thus, the answer is "a".

'''
