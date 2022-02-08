class Tree:
    """Abstract base class representing a tree structure."""

    #------------------------------- nested Position class -------------------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other) # opposite of eq

    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
        """Return Position representing the tree s root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return Position representing p s parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p s children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')
    # ---------- concrete methods implemented in this class ----------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root( ) == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0
    
    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height2(self, p): # time is linear in size of subtree
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """ Return the height of the subtree rooted at Position p.
            If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p) # start height2 recursion
        
class LinkedTree(Tree):

    class _Node: # A private class for storing nodes
        __slots__ = '_element', '_parent', '_children'
        
        def __init__(self, element, parent=None, children=None):
            self._element = element
            self._parent = parent
            self._children = children
            
    class Position(Tree.Position):
        
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node
      
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node: # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None
        
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)
        
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)
        
    def num_children(self, p):
        node = self._validate(p)
        if node._children is None:
            return 0
        else:
            return len(node._children)
        
    def children(self, p):
        node = self._validate(p)
        if node is not None and node._children is not None:
            for child in node._children:
                yield self._make_position(child)
        
    def _add_root(self, e):
        if self._root is not None: raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
        
    def _add_nonroot_node(self, e, p):
        node = self._validate(p)
        if node is None: 
          raise ValueError('No such position exists')
        if node._children is None:
            node._children = []
        for i in range(self.num_children(p)):
            if node._children[i]._element == e: 
              raise ValueError("There is a child with same value.")
        self._size = self._size + 1
        newnode = self._Node(e,node,None)
        node._children = node._children + [newnode] 
        return self._make_position(newnode)
        
    def add_node(self, e, p=None):
        if p == None: 
          return self._add_root(e)
        else: 
          return self._add_nonroot_node(e,p)
 

    def _subtree_preorder(self,p):
        yield p  
        for c in self.children(p):  
            for other in self._subtree_preorder(c):
                yield other

    def _subtree_postorder(self,p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def _traverse_preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p 

    def _traverse_postorder(self):
        if not self.is_empty(): 
            for p in self._subtree_postorder(self.root()):
                yield p           
                
    def all_nodes(self, mode):
        g = None
        if mode == 'pre':
            g = self._traverse_preorder()
        else:
            g = self._traverse_postorder()
        for n in g:
            yield n
            
    def get_path_to_root(self, p):
        if self.is_empty(): 
          raise ValueError("Tree is Empty")
        else:
          arr = []
          while p._node != self._root:
            arr += [p]
            p = self.parent(p)   
          arr.append(self.root())
          return arr

    def find_child_by_value(self, p, value):      
        for i in self.children(p): 
            if i._node._element == value: 
              return i 
        return None 

class ProductCategorizer:
    
    def __init__(self, data_file_path):
        self._data_file_path = data_file_path
        self._tree = None
        

    def fill_tree(self):
      self._tree = LinkedTree()
      filepath = open(self._data_file_path,"r") 
      newline = filepath.readline()
      newline = newline.strip("\n")
      newline = newline.strip()
      root = newline.split(",")[0] 
      self._tree.add_node(root)
      while newline != "": 
        newline = newline.strip("\n")
        newline = newline.strip()
        newline = newline.split(",")
        arr = newline
        node = self._tree.root()
        for i in range(1,len(arr)):
          elements = arr[i]
          element = elements.strip()
          index = self._tree.find_child_by_value(node, element)
          if index == None:
            node = self._tree.add_node(element,node)
          else: 
            node = index
        newline = filepath.readline()
      filepath.close()


    def print_tree(self):
      filepath = open("Assignment2OutputPre.txt","w")
      pre_tree = self._tree.all_nodes("pre")
      for i in pre_tree:
        element = i._node._element
        depth = self._tree.depth(i)
        if depth == 0:
          filepath.write(element)
          filepath.write("\n")
        else:
          n = "\t" * int(depth)
          filepath.write(n)
          filepath.write(element)
          filepath.write("\n")
      filepath.close()
      filepath = open("Assignment2OutputPost.txt","w")
      post_tree = self._tree.all_nodes("post")
      for i in post_tree:
        element = i._node._element
        depth = self._tree.depth(i)
        if depth == 0: 
          filepath.write(element)
          filepath.write("\n")
        else: 
          n = "\t" * int(depth)
          filepath.write(n)
          filepath.write(element)
          filepath.write("\n")
      filepath.close() 
#main
pc = ProductCategorizer('Assignment2Input.txt')
pc.fill_tree()
pc.print_tree()