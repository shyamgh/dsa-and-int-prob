import re 


def revUsingRegex(s):
    rev_list = [word for word in re.split('\s+', s.strip())[::-1]]
    return ' '.join(rev_list)
    

def reverseWords(s):
    rev_list = [word for word in s.strip().split(' ')[::-1] if word]
    return ' '.join(rev_list)


print(reverseWords('   Hello    world    '))
print(revUsingRegex('   Hello    world    '))
