import unittest
import AVLTrees

class CustomAssertions:

    def assertTreeIsBalanced(self, root):
        balance = AVLTrees.getBalance(root)
        #print(balance)
        if balance>1 or balance<-1:
            raise AssertionError('Tree is not balanced')

    def assertTreeProperty(self, root):
        if root.left != None:
            if root.left.key > root.key:
                raise AssertionError('Tree Property is not respected')
            self.assertTreeProperty(root.left)
        if root.right != None:
            if root.right.key < root.key:
                raise AssertionError('Tree Property is not respected')
            self.assertTreeProperty(root.right)

    def assertTree(self, root):
        self.assertTreeIsBalanced(root)
        self.assertTreeProperty(root)


class TestTrees(unittest.TestCase, CustomAssertions):

    def setUp(self):

        print('setUp')
        
        keys = [5, 2, 1, 4, 9, 8, 10]

        self.root1 = None
        
        for key in keys:
            self.root1 = AVLTrees.insert(self.root1, key)

    def test_insert(self):
    
        self.assertTree(AVLTrees.insert(self.root1, 2))
        self.assertTree(AVLTrees.insert(self.root1, 1))

    def test_remove(self):
        
        self.assertTree(AVLTrees.remove(self.root1, 2))
        self.assertTree(AVLTrees.remove(self.root1, 12))

    def test_search(self):

        # Test existing elements
        self.assertTrue(AVLTrees.search(self.root1, 2))
        self.assertTrue(AVLTrees.search(self.root1, 10))

        # Test non existing elements
        self.assertFalse(AVLTrees.search(self.root1, 24))
        self.assertFalse(AVLTrees.search(self.root1, 3))
        


if __name__ == '__main__':
    unittest.main()
