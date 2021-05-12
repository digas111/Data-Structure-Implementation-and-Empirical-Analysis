"""

Código desenvolvido por: Manuel Martins
Num. Mec.: 201504230

Notas: 
  Treap = Tree + Heap
  Heap property
    -> The node v with highest priority must be the node
  Tree property
    -> any node u with key(u) < key (v) must be in the left subtree
    -> any node w with key(w) >= key (v) must be in the right subtree

  A treap is exactly the binary search tree that results 
  of inserting the nodes in order of increasing priority
  into an initially empty tree

  Operations:
    Search:
      - Successful search has time proportional to the depth of the 
        node 
      - Unsuccessful search has time proportional to the depth of
        its predecessor or ancestor

    Insertion: 
      - You do the insertion using the standard BST algorithm
      - At this point you have a BST, but priorities may no 
        longer form a heap
      - As long as the parent ofzhas a smaller priority, you perform 
        a rotation at z, decreasing the depth of z (and increasing 
        the depth of the parent), while keeping the BST property
    

"""

from random import random

class TreapNode(object):
  def __init__(self, data):
    self.left = None 
    self.right = None
    self.data = data
    self.priority = random()

  def printNode(self):
    print("Data: " + str(self.data) + " Priority: " + str(self.priority))

def listInsertTreap(node, dataList):
	for data in dataList:
		node = insertTreap(node,data)
	return node


def insertTreap(node, data):
  if node == None:
    return TreapNode(data)

  elif data < node.data:
    node.left = insertTreap(node.left, data)
    if node.left != None and node.left.priority >= node.priority:
      node = rotateRight(node)

  else:
    node.right = insertTreap(node.right,data)
    if node.right != None and node.right.priority >= node.priority:
      node = rotateLeft(node)

  return(node)

def rotateRight(node):
  auxL = node.left
  auxR = node.left.right

  auxL.right = node
  node.left = auxR 

  return auxL

def rotateLeft(node):
  auxL = node.right.left 
  auxR = node.right

  node.right = auxL 
  auxR.left = node 

  return auxR

def searchTreap(node, data):
  if node == None:
    return False
  elif node.data == data:
    return True
  elif data < node.data:
    return searchTreap(node.left, data)

  return searchTreap(node.right, data)

def deleteTreap(node, data):
  if node == None:
    return None

  elif data < node.data:
    node.left = deleteTreap(node.left, data)

  elif data > node.data:
    node.right = deleteTreap(node.right, data)

  else:
    if node.left == None and node.right == None:
      node = None

    elif node.left == None and node.right != None:
      node = node.right
    elif node.left != None and node.right == None:
      node = node.left
    else:
      if node.left.priority < node.right.priority:
        node = rotateLeft(node)
        node.left = deleteTreap(node.left, data)
      else:
        node = rotateRight(node)
        node.right = deleteTreap(node.right, data)
  
  return node

def printTreap(node, space):
  height = 10

  # Base case
  if node == None :
    print("Entrei")
    return

  # increase distance between levels
  space += height

  # print the right child first
  printTreap(node.right, space)

  # print the current node after padding with spaces
  for i in range(height, space):
    print(' ', end='')

  print((node.data, node.priority))

  # print the left child
  printTreap(node.left, space)

def rangeSearchTreap(node, k1, k2):

  if node == None:
    return

  rangeSearchTreap(node.left, k1, k2)
  
  if k1 <= node.data and node.data <= k2:
    print(" " + str(node.data))

  rangeSearchTreap(node.right, k1, k2)

def getDepht(node):

  if node == None:
    return 0
  
  return 1 + max(getDepht(node.left),getDepht(node.right))


if __name__ == "__main__":
  keys = [5, 2, 1, 4, 9, 8, 10]

    # construct a treap
  node = None
  for key in keys:
    node = insertTreap(node, key)

  print("Constructed :\n\n")
  printTreap(node, 0)

  print("\nDeleting node 1:\n\n")
  node = deleteTreap(node, 1)
  print("fiz delete")
  printTreap(node, 0)

  print("\nDeleting node 5:\n\n")
  node = deleteTreap(node, 5)
  printTreap(node, 0)

  print("\nDeleting node 9:\n\n")
  node = deleteTreap(node, 9)

  printTreap(node, 0)

