# AVL Trees e Treaps Empirical Analysis

## Made by
*Manuel Martins* - up201504230\
*Diogo Ribeiro* - up201504115

## Usage

### Create Tree Database
```
python3 database_generator.py 
```
This generates a .csv file where each row is a list of Integers corresponding to a tree's keys.

### Compare tree Algorithms
```
python3 comparator.py
```
This returns the times that takes the AVL structure and the Treap to insert all nodes in the tree, the depth of the resulting tree. Then 20% of the tree's keys are choosen at random so to be removed from the trees. This elements are printed alongside the time it takes to remove them from each tree structure (AVL and Treap).

Example output for the first tree:
```
Tree 1:
AVL insert time: 0.0012011528015136719
Treap insert time: 0.00045108795166015625
AVL depth: 8
Treap depth: 14
Removing elements: 34 69 45 63 53 20 21 22 35 38 81 82 1 30 89 76 18 7 97 17 
    AVL removing time: 0.0001900196075439453
    Treap removing time: 6.985664367675781e-05
```