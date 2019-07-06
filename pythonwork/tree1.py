class Tree:
    def __init__(self, value):
        self.value=value
        self.left_child = None
        self.right_child = None

    def insert_left_child(self, value):
        if self.left_child == None:
            self.left_child = Tree(value)
        else:
            new_node = Tree(value)
            new_node.left_child = self.left_child
            self.left_child= new_node

    def insert_right_child(self,value):
        if self.right_child == None:
            self.right_child = Tree(value)
        else:
            new_node = Tree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node


# in_order - self, left,right
# pre  - left, self, right
# post order : left, right, self




a_node = Tree('a')
a_node.insert_left_child("b")

b_node = a_node.left_child
b_node.insert_right_child("d")
d_node = b_node.right_child
print(a_node.value)
print(b_node.value)
print(d_node.value)