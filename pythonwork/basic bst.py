class Basic:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def create_tree(self,value):
        if self.value == "":
            self.value = Basic(value)
        elif value <= self.value:
            self.left_child = Basic(value)
        elif value > self.value:
            self.right_child = Basic(value)


new = Basic('5')
new.create_tree('2')
new.create_tree('7')
left_node = new.left_child
right_node = new.right_child
print(left_node.value)
print(right_node.value)
print(new.value)
print(new.right_child)
print(new.left_child)

