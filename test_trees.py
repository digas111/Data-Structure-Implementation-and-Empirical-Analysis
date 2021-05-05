import unittest
import AVLTrees

class CustomAssertions:
    # def assertTreeIsBalanced(self, tree, root):
    #     if tree.getBalance(root) >1 or tree.getBalance(root)<1:
    #         raise AssertionError('Tree is not balanced')
    def assertTreeIsBalanced(self, root):
        if root.left == None and root.right == None:
            return
        if root.left == None:
            balance = 0 - root.right.height
        elif root.right == None:
            balance = root.left.height - 0
        else:
            balance = root.left.height - root.right.height
        if balance >1 or balance<1:
            raise AssertionError('Tree is not balanced')
    def assertTreeProperty(self, root):
        if root.left != None:
            if root.left.val > root.val:
                raise AssertionError('Tree Property is not respected')
            self.assertTreeProperty(root.left)
        if root.right != None:
            if root.right.val < root.val:
                raise AssertionError('Tree Property is not respected')
            self.assertTreeProperty(root.right)
    def assertTree(self, root):
        self.assertTreeIsBalanced(root)
        self.assertTreeProperty(root)


class TestTrees(unittest.TestCase, CustomAssertions):

    @staticmethod
    def balanced(tree):
        pass

    def setUp(self):
        print('setUp')
        self.avlTree1 = AVLTrees.AVL_Tree()
        self.root1 = None
        self.root1 = self.avlTree1.insert(self.root1, 10)
        self.root1 = self.avlTree1.insert(self.root1, 20)
        self.root1 = self.avlTree1.insert(self.root1, 30)
        self.root1 = self.avlTree1.insert(self.root1, 40)
        self.root1 = self.avlTree1.insert(self.root1, 50)
        self.root1 = self.avlTree1.insert(self.root1, 25)

    def test_insert(self):
        self.assertTree(self.avlTree1.insert(self.root1, 2))
        self.avlTree1.PrintTree(self.root1)


if __name__ == '__main__':
    unittest.main()
