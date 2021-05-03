"""
Treap = Tree + Heap
Heap property
-> The node v with highest priority must be the root
Tree property
-> any node u with key(u) < key (v) must be in the left subtree
-> any node w with key(w) > key (v) must be in the left subtree

a treap is exactly the binary search tree that results 
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

class Node:
  


def main():
  print("Hello world")


if __name__ == "__main__":
  main()

