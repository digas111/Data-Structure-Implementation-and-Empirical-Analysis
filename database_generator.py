import random
import csv
import os

def generateTree(size):

    return random.sample(range(1, size+1), size)

def saveToFile(file, tree):

    writer = csv.writer(file)
    writer.writerow(tree)

def deleteDatabase():
    os.remove("treeDatabase.csv")

def main():

    with open('treeDatabase.csv', 'w', newline='') as file:

        saveToFile(file,generateTree(100))
        saveToFile(file,generateTree(1000))
        saveToFile(file,generateTree(10000))
        saveToFile(file,generateTree(1000000))
        saveToFile(file,generateTree(10000000))

    with open('treeDatabase.csv', 'r') as file:
        row_count = sum(1 for row in file)
        print("Created " + str(row_count) + " trees.")



if __name__ == "__main__":
    main()