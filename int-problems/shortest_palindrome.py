'''
Matching palindrome


Problem

You are given a palindrome string P
of length N consisting of only lowercase letters of the English alphabet. Find the shortest non-empty palindrome string Q such that P concatenated with Q forms a palindrome. Formally, the string PQ

forms a palindrome.
Input

The first line of the input gives the number of test cases, T
. T test cases follow. Each test case consists of two lines. The first line of each test case contains an integer N denoting the length of the string P. The second line of each test case contains a palindrome string P of length N

.
Output

For each test case, output one line containing Case  # x
: y, where x is the test case number(starting from 1) and y is the non-empty palindrome string Q

as described above.
Limits

Memory limit: 1 GB.
1≤T≤100
.
String P

is a palindrome consisting of only lowercase letters of the English alphabet.
Test Set 1

Time limit: 20 seconds.
1≤N≤103

.
Test Set 2

Time limit: 40 seconds.
1≤N≤105

.
Sample
Sample Input
save_alt
content_copy

3
4
abba
4
cccc
6
cdccdc

Sample Output
save_alt
content_copy

Case  # 1: abba
Case  # 2: c
Case  # 3: cdc

In Case 1, the shortest palindrome string Q
is abba such that the concatenation PQ is abbaabba which is a palindrome.
In Case 2, the shortest palindrome string Q is c such that the concatenation PQ is ccccc which is a palindrome.
In Case 3, the shortest palindrome string Q is cdc such that the concatenation PQ is cdccdccdc which is a palindrome.
'''

def max_palindrome(s, t):

    res = ''
    mx = 0
    dict1 = {}

    flag = s.count(s[0]) == len(s)

    if flag:
        print('Case #{}: {}'.format(t, s[0]))
        return

    for i in range(len(s)):

        # for odd palindrome strings
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if mx < (r-l+1):
                mx = (r-l+1)
                if s[l:r+1] not in dict1:
                    dict1[s[l:r+1]] = mx
                    res = s[l:r+1]
            l -= 1
            r += 1

        # for even palindrome strings
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if mx < (r-l+1):
                mx = (r-l+1)
                if s[l:r+1] not in dict1:
                    dict1[s[l:r+1]] = mx
                    res = s[l:r+1]
            l -= 1
            r += 1

    mn = len(s) + 1
    for k, v in dict1.items():
        if v < mn and k.count(k[0]) != len(k):
            res = k
            mn = v

    print('Case #{}: {}'.format(t, res))


t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    max_palindrome(s, i+1)
