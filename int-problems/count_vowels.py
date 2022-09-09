# Turing code challange launch - Challenge #2
# How can I find the vowels?
# Date: 04-Aug-2022
# link https://forum.turing.com/post/coding-room/code-challenge-launch-1-whk8o2sjvit2/

# worst case time complexity of O(n)
def count_vowels(s):
    vowels = 'aeiouAEIOU' # vowels in english
    counter = 0

    # add number occurances to dict
    for e in s:
        if e in vowels:
            counter += 1
    
    return counter

if __name__ == "__main__":
    # Sample test cases
    assert(count_vowels("Elephant")) == 3
    assert(count_vowels("car")) == 1
    assert(count_vowels("computer")) == 3
