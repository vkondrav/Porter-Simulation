class BTNode():
	def __init__(self, data):
		self.data = data
		self.delete()
	def delete(self):
		self.left = None
		self.right = None
		self.parent = None
	def printer(self):
		if self.left:
			self.left.printer()
		print self.data,
		if self.right:
			self.right.printer()
	def children(self):
		cnt = 0
		if self.left:
			cnt += 1
		if self.right:
			cnt += 1
		return cnt
		
class BTree():
	def __init__(self):
		self.root = None
		
	def printer(self):
		if self.root == None:
			return 'Empty Tree'
		if self.root.left:
			self.root.left.printer()
		print self.root.data,
		if self.root.right:
			self.root.right.printer()
			
	def isEmpty(self):
		if self.root is None:
			return 1
		else:
			return 0
	
	def insert(self, data):
		newNode = BTNode(data)
		
		if self.root is None:
			self.root = newNode
		else:
			tmpNode = self.root
			while True:
				if data < tmpNode.data:
					if tmpNode.left is None:
						tmpNode.left = newNode
						newNode.parent = tmpNode
						break
					tmpNode = tmpNode.left
				else:
					if tmpNode.right is None:
						tmpNode.right = newNode
						newNode.parent = tmpNode
						break
					tmpNode = tmpNode.right
		return newNode
		
	def lookup(self, data):
		tmpNode = self.root
		while tmpNode is not None:
			if data == tmpNode.data:
				return tmpNode
			elif data < tmpNode.data:
				tmpNode = tmpNode.left
			else:
				tmpNode = tmpNode.right
		return None
			
	def pop(self):
		if self.root is None:
			return None, None
		else:
			returnNode = BTNode
			tmpNode = self.root
			while tmpNode.left is not None:
				tmpNode = tmpNode.left
			
			parent = tmpNode.parent
			returnNode = BTNode(tmpNode.data)
			if tmpNode.children() == 0:
				if tmpNode != self.root:
					if tmpNode.parent.left == tmpNode:
						tmpNode.parent.left = None
					else:
						tmpNode.parent.right = None
				else:
					self.root = None
				tmpNode.delete()
			elif tmpNode.children() == 1:
				if tmpNode.right and tmpNode != self.root:
					tmpNode.parent.left = tmpNode.right
					tmpNode.right.parent = tmpNode.parent
				else:
					self.root = tmpNode.right
					tmpNode.right.parent = None
				tmpNode.delete()
			
			return returnNode,parent