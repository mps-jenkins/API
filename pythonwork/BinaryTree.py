
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self,value):
        if value > self.value and self.right_child:
            self.right_child.insert_node(value)
        elif value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinaryTree(value)
        else:
            self.right_child = BinaryTree(value)

    def find_node(self,value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        elif value > self.value and self.right_child:
            return self.right_child.find_node(value)
        return value == self.value



new_node = BinaryTree('50')
new_node.insert_node('76')
new_node.insert_node('21')
new_node.insert_node('4')
new_node.insert_node('32')
new_node.insert_node('100')

print(new_node.value)
node1 = new_node.left_child
print(node1.value)
node2 = new_node.right_child
print(node2.value)
print(new_node.left_child)
print(new_node.right_child)

print(new_node.find_node('32'))
print(new_node.find_node('222'))