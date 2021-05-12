"""

Código desenvolvido por: Diogo Ribeiro
Num. Mec.: 201504115

Inspired by:
  https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
  https://www.dcc.fc.up.pt/~pribeiro/aulas/taa2021/balancedsearchtrees.pdf 

"""

class AvlNode:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.height = 1

def listInsert(root, keys):
	for key in keys:
		root = insert(root,key)
	return root

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
	if balance < -1 and key >= root.right.key:
		return leftRotation(root)
	if balance > 1 and key >= root.left.key:
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

def rangeSearchTree(root, k1, k2):

	if not root:
		return

	rangeSearchTree(root.left, k1, k2)

	if k1 <= root.key and root.key <= k2:
		print(" " + str(root.key))

	rangeSearchTree(root.right, k1, k2)

def getDepht(root):

	if not root:
		return 0

	return 1 + max(getDepht(root.left),getDepht(root.right))

def main():
	root = None

	keys = [5, 2, 1, 4, 9, 8, 10]
	root = listInsert(root,keys)

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

	for key in keys:
		root = insert(root, key)

	print('balance: ' + str(getBalance(root)))

	rangeSearchTree(root, 3, 10)


if __name__ == "__main__":
    main()