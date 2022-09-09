def decodeString(s):
    num = 0
    str = ''
    stack = []
    
    # Write your code here.
    for c in s:
        if c.isdigit():
            num = num*10 + int(c)
        elif c == '[':
            stack.append(str)
            stack.append(num)
            str = ''
            num = 0
        elif c.isalpha():
            str = str + c
        elif c == ']':
            prev_num = stack.pop()
            prev_str = stack.pop()
            str = prev_str + prev_num * str
            num = 0
    return str

'''
Problem Statement
You have been given an encoded string. Your task is to decode it back to the original string.

- An encoded string will be of the form <count>[encoded_string], where the 'encoded_string' inside the square brackets is being repeated exactly 'count' times. Note that 'count' is guaranteed to be a positive integer and can be greater than 9.
- There are no extra white spaces and square brackets are well-formed.

For example -

Input: 2[a]
“a” is encoded 2 times, hence the decoded string will be "aa".

Input: 3[a2[b]]
“b” is encoded 2 times, which decodes as 3[abb]. Now, "abb" is encoded 3 times, hence decoded string will be "abbabbabb". 

Input Format:

The first line contains an integer 'T' which denotes the number of test cases or queries to be run. Then the test cases follow.

The only line of each test case contains a string 'S' which represents the encoded string. 

Output Format:

For each test case, print a string i.e. the decoded string.

Output for every test case will be printed in a separate line.

Note: You are not required to print the expected output, it has already been taken care of. Just implement the function. 

Constraints:

 1 <= T <= 20
 1 <= |S| <= 500

 where |S| is the length of the Decoded string.

 Time limit: 0.400 sec

Sample Input 1:

2
3[a]2[bc]
a1[b]1[cc]

Sample Output 1:

aaabcbc
abcc

Explanation for sample 1:

For the first test case, "a" is encoded 3 times and "bc" is encoded 2 times. After combining these two strings after decoding, we'll get "aaa" + "bcbc" = "aaabcbc".

Sample Input 2:

1
ab2[c3[b]]

Sample Output 2:

abcbbbcbbb

110.[a12[b]]

'''