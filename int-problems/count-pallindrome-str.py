def palindromicSubstrings(string, n):
    # Write your code here.
    ptr1 = 0
    count = 0

    while ptr1 < n:
        ptr2 = ptr1+1
        while ptr2 <= n:
            if string[ptr1:ptr2] == string[ptr1:ptr2][::-1]:
                count += 1
            ptr2 += 1
        ptr1 += 1

    return count


'''
Problem Statement
You have been given a string STR. Your task is to find the total number of palindromic substrings of STR.
Example:

If the input string is "abbc", then all the possible palindromic substrings would be: ["a", "b", "b", c", "bb"] and hence, the output will be 5 since we have 5 substrings in total which form a palindrome.

Note:

A string is said to be a 'Palindrome' if it is read the same forwards and backwards.
For example, “abba” is a palindrome, but “abbc” is not.

A 'Substring' is a contiguous sequence of characters within a string.
For example, "a", "b", "c", "ab", "bc", "abc" are substrings of "abc".

Input format:

The first line contains an integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first and only line of each test case contains the string STR for which you have to count the number of palindromic substrings.

Output Format:

For each test case, return the total number of palindromic substrings possible.

Output for each test case will be printed in a separate line.

Note

You are not required to print anything, it has already been taken care of. Just implement the function.

Constraints:

1 <= t <= 100
0 <= N <= 1000

Where 't' is the number of test cases, 'N' is the length of the given string.
Time Limit: 1 sec.

Sample Input 1:

1
abc

Sample Output 1:

3

Explanation For Sample Output 1:

All the substrings of the given string are "a", "b", "c", "ab", "bc", "abc".
The plaindromics substrings are "a", "b", "c". So the output will be 3.

Sample Input 2:

1
aaa

Sample Output 2:

6
'''