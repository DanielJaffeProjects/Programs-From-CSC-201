class TreeNode:
  def __init__(self, value, left=None, right=None, parent=None):
    self._value = value
    self._left = left
    self._right = right
    self._parent = parent

  def is_left(self):
    return self._parent and self._parent._left == self

  def is_right(self):
    return self._parent and self._parent._right == self

  def is_root(self):
    return not self._parent

  def is_leaf(self):
    return not (self._left or self._right)

  def has_child(self):
    return self._left or self._right

  def has_children(self):
    return self._left and self._right

  def __str__(self):
    return str(self._value)

class BinarySearchTree:
  def __init__(self):
    self._root = None
    self._size = 0

  def size(self):
    return self._size

  def __len__(self):
    return self._size

def insert(self, val):
  if (not self._root):
    self._root = TreeNode(val)
  else:
    self._insert(val, self._root)
  self._size += 1

def _insert(self, val, node):
  if (val < node._value):
    if (not node._left):
      node._left = TreeNode(val, parent=node)
    else:
      self._insert(val, node._left)
  else:
    if (not node._right):
      node._right = TreeNode(val, parent=node)
    else:
      self._insert(val, node._right)

def print_tree(self, node=None, level=0):
  if (not node):
    node = self._root
  if (node):
    if (node._right):
      self.print_tree(node._right, level + 1)
    print(f"{'    ' * level}{node._value}")
    if (node._left):
      self.print_tree(node._left, level + 1)

def __contains__(self, val):
  return self._search(val, self._root)

def _search(self, val, node=None):
  if (not node):
    return None
  else:
    if (node._value == val):
      return node
    elif (val < node._value):
      return self._search(val, node._left)
    else:
      return self._search(val, node._right)

def delete(self, val, node=None):
  if (self._size == 1 and self._root._value == val):
    self._root = None
    self._size -= 1
    return True
  else:
    node = self._search(val, self._root)
    if (not node):
      return False
    else:
      # case 1: the node is a leaf
      if (node.is_leaf()):
        if (node.is_left()):
          node._parent._left = None
        else:
          node._parent._right = None
      # case 2: the node has one child
      elif (node.has_child() and not node.has_children()):
        # it is a left child
        if (node.is_left()):
          # it has a left child
          if (node._left):
            node._parent._left = node._left
            node._left._parent = node._parent
          # it has a right child
          else:
            node._parent._left = node._right
            node._right._parent = node._parent
        # it is a right child
        elif (node.is_right()):
          # it has a left child
          if (node._left):
            node._parent._right = node._left
            node._left._parent = node._parent
          # it has a right child
          else:
            node._parent._right = node._right
            node._right._parent = node._parent
        # it is the root
        else:
          # it has a left child
          if (node._left):
            self._root = node._left
          # it has a right child
          else:
            self._root = node._right
          self._root._parent = None
        return True
      # case 3: the node has two children
      else:
        # find the successor
        s = node._right
        while (s._left):
          s = s._left
        # get its value
        val = s._value
        # delete the successor
        self.delete(val)
        # replace the current node
        node._value = val
        return True

def __str__(self):
  return self._inorder(self._root)

def _inorder(self, node=None):
  s = ""
  if (node):
    s = str(self._inorder(node._left))
    s += f"{node._value} "
    s += str(self._inorder(node._right))
  return s

