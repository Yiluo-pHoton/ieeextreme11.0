class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def traverse(self, target):
        if self is None:
            return False
        if self.val == target:
            return True
        else:
            for child in self.children:
                traverse(child, target)
    
    def isRelated(self, val1, val2):
        if self.val == val1 or self.val == val2:
            for child in self.children:
                if child.val == val1 or child.val == val2:
                    return True
            return False
        for child in self.children:
            isRelated(child, val1, val2)
        return False

    def __str__(self):
        return str(self.val)
        
map = Node(0)
print(map)
a = int(input())
isLoop = False
for i in range(a):
    n, m = [int(i) for i in input().split()]
    raw = [int(i) for i in input().split()]
    x = raw[0::2]
    fx = raw[1::2]
    map.val = x[0]
    print (x)
    print(fx)
    for i, j in list(list(zip(x, fx))):
        if i == j:
            isLoop = True
            break
        else:
            if map.traverse(i) and not map.traverse(j):
                map.addNode(i)
            elif not map.traverse(i) and map.traverse(j):
                map.addNode(j)
                
print(int(flag))
