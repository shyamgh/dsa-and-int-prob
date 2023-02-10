def reverse_only_alpha(s):

    l = 0
    r = len(s) - 1
    rev = list(s)
    while l < r:
      v1 = ord(s[l])
      v2 = ord(s[r])
      if ((65 <= v1 <= 90) or (97 <= v1 <= 122)) and ((65 <= v2 <= 90) or (97 <= v2 <= 122)):
        tmp = rev[l]
        rev[l] = rev[r]
        rev[r] = tmp
        l += 1
        r -= 1
      else:
        if v1 < 65 or (v1 > 90 and v1 < 97) or v1 > 122:
          l += 1

        if v2 < 65 or (v2 > 90 and v2 < 97) or v2 > 122:
          r -= 1

    new_s = ''.join(rev)
    return new_s


def test_1():
        assert callable(reverse_only_alpha) == True
        print("PASSED: Expect reverse_only_alpha is a function")

def test_2():
    assert reverse_only_alpha("sea!$hells3") == "sll!$ehaes3"
    print(
        "PASSED: Expect reverse_only_alpha('sea!$hells3') to return 'sll!$ehaes3'"
    )

def test_3():
    assert reverse_only_alpha("1kas90jda3") == "1adj90sak3"
    print("PASSED: Expect reverse_only_alpha('1kas90jda3') to return '1adj90sak3'")
    
