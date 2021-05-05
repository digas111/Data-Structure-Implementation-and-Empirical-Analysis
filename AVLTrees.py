#AVL Tree implementation

class AvlNode:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.height = 1

def insert(root, key):

	if not root:
		return AvlNode(key)
	elif key < root.key:
		root.left = insert(root.left, key)
	else:
		root.right = insert(root.right, key)

	root.height = 1 + max(getHeight(root.left),getHeight(root.right))

	balance = getBalance(root)

	if balance > 1 and key < root.left.key:
		return rightRotation(root)
	if balance < -1 and key > root.right.key:
		return leftRotation(root)
	if balance > 1 and key > root.left.key:
		root.left = leftRotation(root.left)
		return rightRotation(root)
	if balance < -1 and key < root.right.key:
		root.right = rightRotation(root.right)
		return leftRotation(root)

	return root

def remove(root,key):

	if not root:
		return

	if root is None:
		return root
	
	if key < root.key:
		root.left = remove(root.left,key)
	elif key > root.key:
		root.right = remove(root.right,key)

	else:
		if root.left is None:
			temp = root.right
			root = None
			return temp
		elif root.right is None:
			temp = root.left
			root = None
			return temp
		
		temp = getMinValueNode(root.right)
		root.key = temp.key
		root.right = remove(root.right,temp.key)

	root.height = 1 + max(getHeight(root.left),getHeight(root.right))

	balance = getBalance(root)

	if balance >1 and getBalance(root.left)>=0:
		return rightRotation(root)
	elif balance < -1 and getBalance(root.right)<=0:
		return leftRotation(root)
	elif balance > 1 and getBalance(root.left) < 0:
		root.left = leftRotation(root.left)
		return rightRotation(root)
	elif balance < -1 and getBalance(root.right) > 0:
		root.right = rightRotation(root.right)
		return leftRotation(root)

	return root

def getMinValueNode(root):
	if root is None or root.left is None:
		return root
	return getMinValueNode(root.left)

def rightRotation(z):

	y = z.left
	x = y.right

	y.right = z
	z.left = x

	z.height = 1 + max(getHeight(z.left),getHeight(z.right))
	y.height = 1 + max(getHeight(y.left),getHeight(y.right))

	return y

def leftRotation(z):

	y = z.right
	x = y.left

	y.left = z
	z.right = x

	z.height = 1 + max(getHeight(z.left),getHeight(z.right))
	y.height = 1 + max(getHeight(y.left),getHeight(y.right))

	return y

def getHeight(root):

	if not root:
		return 0
	return root.height

def getBalance(root):
	if not root:
		return 0
	
	return getHeight(root.left) - getHeight(root.right)

def search(root,key):
	if not root:
		return False

	if key > root.key:
		return search(root.right,key)

	if key < root.key:
		return search(root.left,key)

	return True


def treeArray(root):
	if not root:
		return ""
	return treeArray(root.left) + str(root.key) + " " + treeArray(root.right)

def PrintTree(root):

	if not root:
		return

	PrintTree(root.left)
	print( root.key, end =" ")
	PrintTree(root.right)

#    4
#   / \
#  /   \
#  5   4
# / \ / \
# 5 8 4 5

def main():
	root = None

	root = insert(root, 12)
	root = insert(root, 6)
	root = insert(root, 14)
	root = insert(root, 3)
	root = insert(root, 2)
	root = insert(root, 1)

	print(treeArray(root))

	print(search(root,5))

	root = remove(root, 3)
	print(treeArray(root))
	root = remove(root, 12)
	print(treeArray(root))
	root = remove(root, 6)
	print(treeArray(root))
	root = remove(root, 14)
	print(treeArray(root))
	root = remove(root, 2)
	print(treeArray(root))
	root = remove(root, 1)
	print(treeArray(root))

	

	# PrintTree(root)
	# print("")
	print('balance: ' + str(getBalance(root)))


if __name__ == "__main__":
    main()