#AVL Tree implementation

class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1

class AVL_Tree(object):

	#insert node
	def insert(self, root, key):

		if not root:
			return Node(key)
		elif key < root.val:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		#update height
		root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

		balance = self.getBalence(root)

		#Rigth is higher
		if balance > 1:
			if key < root.right:
				self.rightRotation(root.right)
			return self.leftRotation(root)

		#Left is higher
		elif balance < -1:
			if key > root.left.val:
				self.leftRotation(root.left)
			return self.rightRotation(root)
		
		return root
			
	def getHeight(self, root):
		if not root:
			return 0
		return root.height

	def getBalence(self, root):
		if not root:
			return 0
		
		return self.getHeight(root.right) - self.getHeight(root.left)

	def rightRotation(self, a):

		b = a.left
		a.left = b.right
		b.right = a

		a.height = 1 + max(self.getHeight(a.left),self.getHeight(a.right))
		b.height = 1 + max(self.getHeight(b.left),self.getHeight(b.right))

		return b

	def leftRotation(self, a):

		b = a.right
		a.right = b.left
		b.left = a

		a.height = 1 + max(self.getHeight(a.left),self.getHeight(a.right))
		b.height = 1 + max(self.getHeight(b.left),self.getHeight(b.right))

		return b


	#balance tree