class Bst:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self,value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = Bst(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = Bst(value)

node1 = Bst('100')
node1.insert_node('30')
node1.insert_node('20')
node1.insert_node('40')
node1.insert_node('70')
node1.insert_node('60')

node2 = node1.left_child
print(node2.value)
node3 = node1.right_child
print(node3.value)


node4= node3.right_child
print(node4.value)
node5 = node4.right_child
print(node5.value)
node7 = node5.right_child
print(node7.value)

