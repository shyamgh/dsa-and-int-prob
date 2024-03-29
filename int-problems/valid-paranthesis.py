def isValidParenthesis(expression):
    # Write your code here.
    stack = []
    for c in expression:
        if c in ['{', '[', '(']:
            stack.append(c)
        elif c in ['}', ']', ')']:
            if len(stack) == 0:
                return False
            c1 = stack.pop()
            if c == '}' and c1 != '{':
                return False
            elif c == ']' and c1 != '[':
                return False
            elif c == ')' and c1 != '(':
                return False
    return (len(stack) == 0)


# Main Code
t = int(input().strip())
for i in range(t):
    str = input().strip()
    ans = isValidParenthesis(str)
    if ans:
        print("Balanced")
    else:
        print("Not Balanced")


'''
You're given string ‘STR’ consisting solely of “{“, “}”, “(“, “)”, “[“ and “]” . Determine whether the parentheses are balanced.
Input Format:

The first line contains an Integer 'T' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first and the only line of input of each test case contains a string, as described in the task.

Output format :

For each test case, the first and the only line of output prints whether the string or expression is balanced or not.

The output of every test case is printed in a separate line.

Note:

You are not required to print anything explicitly. It has already been taken care of. Just implement the given function.

Constraints:

1 <= T <= 10
1 <= N <= 10^5

Where N is the length of the input string or expression.

Time Limit: 1 sec

Sample Input 1 :

2
[()]{}{[()()]()}
[(])

Sample Output 1 :

Balanced
Not Balanced

Explanation Of the Sample Input 1 :

In TestCase 1 there is always an opening brace before a closing brace i.e ‘{‘ before ‘}’, ‘(‘ before ‘)’, ‘[‘ before ‘]’.

In TestCase 2 there is closing brace for ‘[‘ i.e. ‘]’ before closing brace for ‘(‘ i.e. ‘)’. The balanced sequence should be ‘[()]’.

Sample Input 2 :

2
[[}[
[]{}()

Sample Output 2 :

Not Balanced
Balanced

Explanation Of the Sample Input 2 :

In TestCase 1 there is no opening brace before a closing brace i.e no ‘{‘ for ‘}’.

In TestCase 2 there is exactly one closing for each opening braces and each closing brace is after their corresponding opening brace.

'''
