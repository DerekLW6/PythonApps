from TreeNode import TreeNode

# # Testing of the tree node
root = TreeNode('Founder')
child_a = TreeNode('VP of Bananas')
child_b = TreeNode('Executive Assistant')
child_c = TreeNode('Banana R & D')

# adding children to the root
root.add_child(child_a)
root.add_child(child_b)

# # assigning child_c to child_a creates an additional level in the tree
child_a.add_child(child_c)

# # prints "Founder", "VP of Bananas", "Executive Assistant"
root.traverse()
