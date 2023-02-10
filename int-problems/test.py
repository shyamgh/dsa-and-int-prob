class A():
    
    def m(self, a=''):
        print(f"A{a}")


class B(A):

    def m(self, a=''):
        # super().m(a)
        print(f"B{a}")
        
o = B()
o.m('hello')
