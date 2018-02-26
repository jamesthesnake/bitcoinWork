class RBTree:
    __slots__ = {'_root'}

    def __init__(self):
        self._root = None

    def insert(self, data):
        if(self._root is None):
            self._root = Node(data, None, 0)
        else:
            self._insert(Node(data, None, 0))

    def _insert(self, z):
        y = None
        x = self._root
        while(x is not None):
            y = x
            if(z.data < x.data):
                x = x.left
            else:
                x = x.right
        z.parent = y
        if(y is None):
            self._root = z
        elif(z.data < y.data):
            y.left = z
        else:
            y.right = z

        z.left = None
        z.right = None
        z.color = 1
        self._insertFix(z)

    def _insertFix(self, z):
        print("Print z from _insertFix: " + str(z.data) + "\n")
        while(z.parent.color is 1):
            if(z.parent == z.parent.parent.left):
                y = z.parent.parent.right
                if(y.color is 1):
                    z.parent.color = 0
                    y.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if(z == z.parent.right):
                        z = z.parent
                        self._rotateLeft(z)
                    z.parent.color = 0
                    z.parent.parent = 1
                    self._rotateRight(z.parent.parent)
            else:
                y = z.parent.parent.left
                if(y.color is 1):
                    z.parent.color = 0
                    y.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if(z == z.parent.left):
                        z = z.parent
                        self._rotateRight(z)
                    z.parent.color = 0
                    z.parent.parent = 1
                    self._rotateLeft(z.parent.parent)
        self._root.color = 0

    def _rotateLeft(self, x):
        y = x.right
        x.right = y.left
        if(y.left is not None):
            y.left.parent = x
        y.parent = x.parent
        if(x.parent is not None):
            self._root = y
        elif(x == x.parent.left):
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotateRight(self, x):
        x = y.left
        y.left = x.right
        if(x.right is not None):
            x.right.parent = y
        x.parent = y.parent
        if(y.parent is None):
            self._root = x
        elif(y == y.parent.right):
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

class Node:
    __slots__ = {"_left", "_right", "_parent", "_data", "_color"}
if __name__ == "__main__":
    tree1 = RBTree()
    tree2 = RBTree()

    for x in (3, 5, 6, 7):
        tree1.insert(x)

    for x in (5, 3, 6, 2):
        tree2.insert(x)

    print "done"
