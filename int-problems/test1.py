import pytest

class TestA:
    
    def setup_class(self):
        print('before class')
    
    def teardown_class():
        print('after class')

    def setup_method(self):
        print('before method')

    def teardown_method(self):
        print('after method')
        
    def test1(self):
        print('Test1')

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())



@pytest.fixture
def get_num():
    return 10

def test_fixture(get_num):
    assert get_num == 9

pytest.main()

def find_index(arr):
    
    if len(arr) <= 2:
        return -1
    
    l = 0
    r = 0
    
    for i in range(1, len(arr)):
        l, r = i-1, i+1
        
        lsum = 0
        rsum = 0
        
        while l>=0:
            lsum += arr[l]
            l -= 1
        
        while r<len(arr):
            rsum += arr[r]
            r += 1
        
        if lsum == rsum:
            return arr[i]
    
    return -1

print(find_index([1, 3, 5, 2, 2]))

print(find_index([1, 3]))

print(find_index([9, 3, 5, 2, 1]))


class A:
    
    @staticmethod
    def sm():
        print('static method')
    
A.sm()