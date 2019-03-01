class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  # start at root node, explore as far on each branch before back tracking
  def depth_first_for_each(self, cb):
    pass    

  # call anon function on each in breadth first order
  # traverse nodes in order
  # HINT: probably want to utilize a Queue data structure (FIFO)
  # put first node in queue --> pop --> if left child push, if right child push --> continue
  def breadth_first_for_each(self, cb):
    queue = [self]

    while True:
      # if node in queue
      if len(queue):
        # take front node
        current = queue.pop(0)

        # check children
        if current.left:
          queue.append(current.left)
        if current.right:
          queue.append(current.right)

        # run anon function
        cb(current.value)
      else:
        break




  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
