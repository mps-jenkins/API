

class BinaryTree:
      def __init__(self, value):
          self.value = value
          self.left_child= None
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


bst = BinaryTree(15)
bst.insert_node(10)
bst.insert_node(8)
bst.insert_node(12)
bst.insert_node(20)
bst.insert_node(17)
bst.insert_node(25)
bst.insert_node(19)

print(bst.value)
right = bst.right_child
print(right.value)

print(bst.find_node(8))