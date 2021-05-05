#AVL Tree implementation

class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1

class AVL_Tree(object):

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1

	#insert node
	def insert(self, root, val):

		if not root:
			return Node(val)
		elif val < root.val:
			root.left = self.insert(root.left, val)
		else:
			root.right = self.insert(root.right, val)

		root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

		balance = self.getBalance(root)

		if balance > 1 and val < root.left.val:
			return self.rightRotation(root)
		if balance < -1 and val > root.right.val:
			return self.leftRotation(root)
		if balance > 1 and val > root.left.val:
			root.left = self.leftRotation(root.left)
			return self.rightRotation(root)
		if balance < -1 and val < root.right.val:
			root.right = self.rightRotation(root.right)
			return self.leftRotation(root)

		return root

	def rightRotation(self, z):

		y = z.left
		x = y.right

		y.right = z
		z.left = x

		z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

		return y

	def leftRotation(self, z):

		y = z.right
		x = y.left

		y.left = z
		z.right = x

		z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

		return y

	def getHeight(self, root):

		if not root:
			return 0
		return root.height

	def getBalance(self, root):
		if not root:
			return 0
		
		return self.getHeight(root.left) - self.getHeight(root.right)

	def PrintTree(self, root):

		if not root:
			return

		self.PrintTree(root.left)
		print( root.val, end =" ")
		self.PrintTree(root.right)

#    4
#   / \
#  /   \
#  5   4
# / \ / \
# 5 8 4 5

def main():
	myTree = AVL_Tree()
	root = None

	root = myTree.insert(root, 12)
	root = myTree.insert(root, 6)
	root = myTree.insert(root, 14)
	root = myTree.insert(root, 3)
	root = myTree.insert(root, 2)
	root = myTree.insert(root, 1)

	myTree.PrintTree(root)
	print("")
	print('balance: ' + str(myTree.getBalance(root)))


if __name__ == "__main__":
    main()