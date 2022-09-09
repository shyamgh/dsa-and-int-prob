# Turing code challange launch - Challenge #1
# How to detect two distinct elements
# Date: 04-Aug-2022
# link https://forum.turing.com/post/coding-room/code-challenge-launch-1-whk8o2sjvit2/

# worst case time complexity of O(n)
def return_uniques(arr):
    unq_list = [] # to store unique numbers
    dict1 = {} # dictionary for each number and its occurances

    # add number occurances to dict
    for e in arr:
        if e in dict1:
            dict1[e] = dict1[e] + 1
        else:
            dict1[e] = 1

    # add unique numbers to list
    for k,v in dict1.items():
        if v == 1:
            unq_list.append(k)
    
    return unq_list

if __name__ == "__main__":
    # Sample test cases
    assert(return_uniques([1, 1, 2, 2, 3, 3, 4, 5, 5, 6])) == [4, 7]
    assert(return_uniques([9, 9, 2, 3, 3, 3, 4, 4, 10, 10, 6])) == [2, 6]
    assert(return_uniques([10, 10, 90, 90, 30, 45, 45, 6, 6,
                   6, 6, 6, 6, 1])) == [30, 1]
