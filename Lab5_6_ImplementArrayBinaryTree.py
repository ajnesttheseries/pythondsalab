from Lab5_5_ArrayBinaryTree import ArrayBinaryTree
T = ArrayBinaryTree()
print('# T:', len(T))

# test udpate methods
nodes = []
nodes.append(T._add_root('0'))
nodes.append(T._add_left(nodes[0], '1'))
nodes.append(T._add_right(nodes[0], '2'))
print('# T:', len(T))
print('height:', T.height())
nodes.append(T._add_left(nodes[1], '3'))
nodes.append(T._add_right(nodes[1], '4'))
nodes.append(T._add_left(nodes[2], '5'))
nodes.append(T._add_right(nodes[2], '6'))
nodes.append(T._add_left(nodes[3], '7'))
nodes.append(T._add_right(nodes[4], '10'))
nodes.append(T._add_right(nodes[6], '14'))
print('# T:', len(T))
print('height:', T.height())

print(nodes)
# test public access methods
for i in range(len(T)):
    p = nodes[i]
    parent = T.element(T.parent(p)) if T.parent(p) is not None else 'None'
    left = T.element(T.left(p)) if T.left(p) is not None else 'None'
    right = T.element(T.right(p)) if T.right(p) is not None else 'None'
    num_children = T.num_children(p)
    print('p' + str(i) + ': ' + str(T.element(p)), 
          'parent: ' + str(parent),
          'left: ' + str(left),
          'right: ' + str(right),
          'children: ' + str(num_children))

# test replace
old = T._replace(nodes[0], '-1')
print('Replace ' + old + ' to ' + T.element(nodes[0]))

print('node positions:', nodes)

# test depth and height
print('Depth at p6:', T.depth(nodes[6]))
print('Height at p6:', T.height(nodes[6]))
