from Lab5_3_LinkedBinaryTree import LinkedBinaryTree

T = LinkedBinaryTree()
print('# T:', len(T))

# test udpate methods
nodes = []
nodes.append(T._add_root('0'))
nodes.append(T._add_left(nodes[0], '1'))
nodes.append(T._add_right(nodes[0], '2'))
print('# T:', len(T))

nodes.append(T._add_left(nodes[1], '3'))
nodes.append(T._add_right(nodes[1], '4'))
nodes.append(T._add_left(nodes[2], '5'))
nodes.append(T._add_right(nodes[2], '6'))
print('# T:', len(T))

# test public access methods
for i in range(len(T)):
    node = nodes[i]
    element = node.element()
    parent = T.parent(node).element() if T.parent(node) is not None else 'None'
    left = T.left(node).element() if T.left(node) is not None else 'None'
    right = T.right(node).element() if T.right(node) is not None else 'None'
    num_children = T.num_children(node)
    print('p' + str(i) + ': ' + element, 
          'parent: ' + parent,
          'left: ' + left,
          'right: ' + right,
          'children: ' + str(num_children))

# test replace
old = T._replace(nodes[0], '-1')
print('Replace ' + old + ' to ' + nodes[0].element())

# test delete
T._delete(nodes[5])
print('node 2 left child:', T.left(nodes[2]))
print('node 2 children:', T.num_children(nodes[2]))
T._add_left(nodes[2], '5')
print('node 2 left child:', T.left(nodes[2]).element())

# test depth and height
print('depth at p6:', T.depth(nodes[6]))
print('height:', T.height())

