class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
		
	def insert(self, data):
		#calls node recursively to insert into proper place
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
			else:
				self.data = data	
				
	def lookup(self, data, parent=None):
		if data < self.data:
			if self.left is None:
				return None, None
			return self.left.lookup(data, self)
		elif data > self.data:
			if self.right is None:
				return None, None
			return self.right.lookup(data, self)
		else:
			return self, parent
			
	def delete(self, data):
		node, parent = self.lookup(data)
		if node is not None:
			children_count = node.children_count()
		if children_count == 0:
			if parent:
				if parent.left is node:
					parent.left = None
				else:
					parent.right = None
				del node
			else: self.data = None
			
		elif children_count == 1:
			#if node has 1 child replace with the child
			if node.left:
				n = node.left
			else:
				n = node.right
			if parent:
				if parent.left is node:
					parent.left = n
				else:
					parent.right = n
				del node
			else:
				self.left = n.left
				self.right = n.right
				self.data = n.data
		
		else:
			parent = node
			successor = node.right
			while successor.left:
				parent = successor
				successor = successor.left
				
			node.data = successor.data
			if parent.left == successor:
				parent.left = successor.right
			else:
				parent.right = successor.right
				
	def print_tree(self):
		if self.left:
			self.left.print_tree()
		print self.data,
		if self.right:
			self.right.print_tree()
			
	def children_count(self):
		cnt = 0
		if self.left:
			cnt += 1
		if self.right:
			cnt += 1
		return cnt
		
	def compare_trees(self, node):
		if node is None:
			return False
		if self.data != node.data:
			return False
		res = True
		if self.left is None:
			if node.left:
				return False
		else:
			res = self.left.compare_trees(node.left)
		if res is False:
			return False
		if self.right is None:
			if node.right:
				return False
		else:
			res = self.right.compare_trees(node.right)
		return res
		
	def tree_data(self):
		stack = []
		node = self
		while stack or node:
			if node:
				stack.append(node)
				node = node.left
			else:
				node = stack.pop()
				yield node.data
				node = node.right
				
		