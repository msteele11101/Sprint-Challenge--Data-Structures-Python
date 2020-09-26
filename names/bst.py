class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):

        if self.value == target:
            return True
        else:
            if target < self.value:
                if self.left:
                    return self.left.contains(target)

            if target > self.value:
                if self.right:
                    return self.right.contains(target)
        return False

    def get_max(self):

        if not self.right:
            return self.value
        return self.right.get_max()

    def for_each(self, fn):

        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
