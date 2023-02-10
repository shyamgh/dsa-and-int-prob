
class Tree():
    
    def __init__(self, value, left, right):
        self.left = left
        self.value = value
        self.right = right
    
    

t1 = Tree(5, None, None)
t2 = Tree(6, None, None)
t3 = Tree(1, t1, t2)

