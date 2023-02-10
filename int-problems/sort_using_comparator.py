from functools import cmp_to_key

def factors(a):
    ans = 0    
    for i in range(1, a+1):
        if a % i == 0:
            ans += 1
    return ans
    

def compare(a, b):
    if factors(a) > factors(b):
        return 1
    elif factors(a) < factors(b):
        return -1
    elif factors(a) == factors(b):
        if a > b:
            return 1
        else:
            return -1

def custom_sort(A):    
    return sorted(A, key=cmp_to_key(compare))


def test_sort():
    assert custom_sort([3, 8, 16, 5, 2, 25]) == [2, 3, 5, 25, 8, 16]
    
    

def firstUniqueChar(s):
    d = {
        
    }
    
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    
    for k, v in d.items():
        if v == 1:
            return k
        
    


# print(firstUniqueChar(s='acabdebebzwqc'
#                       ))

# d = {}
# d[5] = 'a'
# d[2] = 'c'
# d[1] = 'k'

# print(d)


def compare2(a, b):
    if ord(a) > ord(b):
        return -1
    else:
        return 1

print(sorted('abcqwieuyksjxcbas', key=cmp_to_key(compare2)))
