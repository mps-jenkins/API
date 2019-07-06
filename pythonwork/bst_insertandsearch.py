
class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinaryTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinaryTree(value)

    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)
        return value == self.value

    def delete_node(self, value):


bst = BinaryTree(50)
bst.insert_node(15)
bst.insert_node(45)
bst.insert_node(11)
bst.insert_node(79)
bst.insert_node(90)
bst.insert_node(99)
bst.insert_node(1)
bst.insert_node(13)


node2 = bst.left_child
node3 = bst.right_child
node8 = node3.right_child
node9 = node8.right_child

node4 = node2.left_child
node5 = node2.right_child
node6 = node4.left_child
node7 = node4.right_child

#print(node9.value)
print(bst.find_node(2))


