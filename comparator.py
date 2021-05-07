import AVLTrees
import Treap
import csv
import time
import random

def compareOperations(tree):

        # Insert #

    # AVL Tree
    start = time.time()
    avlRoot = None
    avlRoot = AVLTrees.listInsert(avlRoot,tree)
    stop = time.time()
    print("AVL insert time: " + str(stop-start))

    # Treap Tree
    start = time.time()
    treapRoot = None
    treapRoot = Treap.listInsertTreap(treapRoot,tree)
    stop = time.time()
    print("Treap insert time: " + str(stop-start))

        # Remove #

    ncases = int(0.2*len(tree))
    keys = random.sample(range(1,len(tree)),ncases)

    print("Removing elements:",end=" ")
    for key in keys:
        print(key,end=" ")
    print("")

    start = time.time()
    for key in keys:
        avlRoot = AVLTrees.remove(avlRoot,int(key))
    stop = time.time()

    print("    AVL removing time: " + str(stop-start))

    start = time.time()
    for key in keys:
        treapRoot = Treap.deleteTreap(treapRoot,key)
    stop = time.time()
    print("    Treap removing time: " + str(stop-start))

def main():

    with open('treeDatabase.csv', 'r') as file:
        csv_reader = csv.reader(file)
        i = 1
        for row in csv_reader:
            print("Tree " + str(i) + ":")
            intRow = []
            for col in row:
                intRow.append(int(col))
            compareOperations(intRow)
            i+=1

if __name__ == "__main__":
    main()