from Node import Node
from LinkedList import LinkedList

# Adding code
node_1 = Node(44)
node_2 = Node(33)
node_3 = Node(22)

ll = LinkedList(4)
ll.insert_beginning(3)
ll.insert_beginning(2)
ll.insert_beginning(6)
ll.remove_node(2)
print(ll.stringify_list())