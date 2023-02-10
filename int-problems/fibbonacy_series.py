
def fib(n):
    
    if n == 1:
        print(1)
    if n == 2:
        print('1 1')
    
    n1 = 1
    n2 = 1
    
    print(n1, end=' ')
    print(n2, end=' ')
    
    for i in range(3, n+1):
        n3 = n1+n2
        print(n3, end=' ')

        n1 = n2
        n2 = n3    


fib(8)    
print('')