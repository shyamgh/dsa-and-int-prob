
# You have array of N integers
# in one operation A[i] = -1
# Return minimum number OF operations such that Max element of array will be B
# if not possible return I

# Example 
# A = [2, 4, 3, 1, 5]
# B = 3

import pytest

def solve(A, B):
    
    is_element_present = False
    ans = 0
    
    for i in A:
        if i == B:
            is_element_present = True
        elif i > B:
            ans += 1
    
    if not is_element_present:
        return -1
    else:
        return ans

def test_solve1():
    assert solve([2, 4, 3, 6, 1, 5], 3) == 3


def test_solve2():
    assert solve([2, 4, 6, 1, 5], 3) == -1

pytest.main()