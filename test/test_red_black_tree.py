import unittest
from bin_tree.red_black_tree import TreeSet, TreeDict, Color


class Insert(unittest.TestCase):
    def test_simple(self):
        tree = TreeSet()
        for _ in (2, 1, 3):
            tree.add(_)
        self.assertEqual(Color.BLACK, tree.root.color)
        self.assertEqual(Color.RED, tree.root.left.color)
        self.assertEqual(Color.RED, tree.root.right.color)
        self.assertEqual(2, tree.height())
        self.assertEqual(1, tree.black_height())
        self.assertTrue(tree.is_valid())

    def test_swap(self):
        tree = TreeSet()
        for _ in (2, 1, 3):
            tree.add(_)
        tree.add(4)
        self.assertEqual(Color.BLACK, tree.root.color)
        self.assertEqual(Color.BLACK, tree.root.left.color)
        self.assertEqual(Color.BLACK, tree.root.right.color)
        self.assertEqual(Color.RED, tree.root.right.right.color)
        self.assertTrue(tree.is_valid())

    def test_left(self):
        tree = TreeSet()
        for _ in (2, 1, 3, 4):
            tree.add(_)
        tree.add(5)
        self.assertEqual(4, tree.root.right.key)
        self.assertEqual(Color.RED, tree.root.right.color)
        self.assertEqual(Color.BLACK, tree.root.right.left.color)
        self.assertEqual(Color.BLACK, tree.root.right.right.color)
        self.assertEqual(list(range(1, 6)), list(tree))
        self.assertTrue(tree.is_valid())

    def test_right(self):
        tree = TreeSet()
        for _ in (4, 3, 5, 2):
            tree.add(_)
        tree.add(1)
        self.assertEqual(2, tree.root.left.key)
        self.assertEqual(Color.RED, tree.root.left.color)
        self.assertEqual(Color.BLACK, tree.root.left.left.color)
        self.assertEqual(Color.BLACK, tree.root.left.right.color)
        self.assertEqual(list(range(1, 6)), list(tree))
        self.assertTrue(tree.is_valid())

    def test_double_left(self):
        tree = TreeSet()
        for _ in (2, 1, 3, 5):
            tree.add(_)
        tree.add(4)
        self.assertEqual(4, tree.root.right.key)
        self.assertEqual(Color.RED, tree.root.right.color)
        self.assertEqual(Color.BLACK, tree.root.right.left.color)
        self.assertEqual(Color.BLACK, tree.root.right.right.color)
        self.assertEqual(list(range(1, 6)), list(tree))
        self.assertTrue(tree.is_valid())


class Delete(unittest.TestCase):
    def test_red_single(self):
        tree = TreeSet((2, 1, 5, 3))
        tree.discard(3)
        self.assertEqual(2, tree.black_height())
        self.assertEqual(2, tree.height())
        self.assertEqual((1, 2, 5), tuple(tree))
        self.assertTrue(tree.is_valid())

    def test_root_right(self):
        tree = TreeSet()
        for _ in (2, 1, 4, 3, 5, 6):
            tree.add(_)
        self.assertEqual(2, tree.black_height())
        self.assertEqual(4, tree.height())
        tree.discard(2)
        self.assertEqual(3, tree.root.key)
        self.assertEqual(5, tree.root.right.key)
        self.assertEqual(Color.RED, tree.root.right.color)
        self.assertEqual(Color.BLACK, tree.root.right.left.color)
        self.assertEqual(Color.BLACK, tree.root.right.right.color)
        self.assertTrue(tree.is_valid())

    def test_root_left(self):
        tree = TreeSet()
        for _ in (5, 3, 6, 1, 4, 2):
            tree.add(_)
        self.assertEqual(2, tree.black_height())
        self.assertEqual(4, tree.height())
        tree.discard(5)
        self.assertEqual(4, tree.root.key)
        self.assertEqual(2, tree.root.left.key)
        self.assertEqual(Color.RED, tree.root.left.color)
        self.assertEqual(Color.BLACK, tree.root.left.left.color)
        self.assertEqual(Color.BLACK, tree.root.left.right.color)
        self.assertTrue(tree.is_valid())

    def test_black_one_red_child(self):
        tree = TreeSet()
        for _ in (4, 2, 6, 1, 3, 5, 8, 7):
            tree.add(_)
        self.assertEqual(2, tree.black_height())
        tree.discard(8)
        self.assertEqual(Color.BLACK, tree.root.right.right.color)
        self.assertTrue(tree.is_valid())

    def test_red_parent(self):
        tree = TreeSet()
        for _ in (4, 2, 8, 1, 3, 6, 10, 5, 7, 9):
            tree.add(_)
        self.assertEqual(2, tree.black_height())
        tree.discard(9)
        tree.discard(10)
        self.assertEqual(2, tree.black_height())
        self.assertEqual(Color.RED, tree.root.right.color)
        self.assertEqual(Color.BLACK, tree.root.right.right.color)
        self.assertEqual(Color.BLACK, tree.root.right.left.color)
        self.assertEqual(Color.RED, tree.root.right.right.left.color)
        self.assertTrue(tree.is_valid())

    def test_all_black(self):
        tree = TreeSet()
        for _ in (1, 2, 3, 4, 5, 6, 7):
            tree.add(_)
        self.assertEqual(3, tree.black_height())
        self.assertEqual(3, tree.height())
        tree.discard(7)
        self.assertEqual(2, tree.black_height())
        self.assertEqual(4, tree.root.key)
        self.assertEqual(Color.RED, tree.root.left.color)
        self.assertEqual(Color.BLACK, tree.root.right.color)
        self.assertEqual(Color.RED, tree.root.right.left.color)
        self.assertEqual(None, tree.root.right.right)
        self.assertTrue(tree.is_valid())

    def test_black_sibling_red_child(self):
        tree = TreeSet()
        for _ in (1, 2, 3, 4, 6, 8, 9):
            tree.add(_)
        self.assertEqual(3, tree.black_height())
        self.assertEqual(3, tree.height())
        tree.add(5)
        tree.add(7)
        self.assertEqual(3, tree.black_height())
        self.assertEqual(4, tree.height())
        tree.discard(9)
        self.assertEqual(3, tree.black_height())
        self.assertEqual(4, tree.height())
        self.assertEqual(4, tree.root.key)
        self.assertEqual(6, tree.root.right.key)
        self.assertEqual(Color.BLACK, tree.root.right.color)
        self.assertEqual(5, tree.root.right.left.key)
        self.assertEqual(Color.BLACK, tree.root.right.left.color)
        self.assertEqual(8, tree.root.right.right.key)
        self.assertEqual(Color.BLACK, tree.root.right.right.color)
        self.assertEqual(7, tree.root.right.right.left.key)
        self.assertEqual(Color.RED, tree.root.right.right.left.color)
        self.assertTrue(tree.is_valid())

    def test_red_sibling(self):
        tree = TreeSet()
        for _ in (1, 2, 3, 4, 6, 9, 10, 5, 7, 8):
            tree.add(_)
        self.assertEqual(3, tree.black_height())
        tree.discard(10)
        self.assertEqual(6, tree.root.right.key)
        self.assertEqual(Color.BLACK, tree.root.right.color)
        self.assertEqual(8, tree.root.right.right.key)
        self.assertEqual(Color.RED, tree.root.right.right.color)
        self.assertEqual(7, tree.root.right.right.left.key)
        self.assertEqual(Color.BLACK, tree.root.right.right.left.color)
        self.assertEqual(9, tree.root.right.right.right.key)
        self.assertEqual(Color.BLACK, tree.root.right.right.right.color)
        self.assertTrue(tree.is_valid())


class Validation(unittest.TestCase):
    def test_red_root(self):
        tree = TreeSet()
        for _ in (1, 2, 3):
            tree.add(_)
        tree.root.color = Color.RED
        self.assertTrue(tree.root.is_valid())
        self.assertFalse(tree.is_valid())

    def test_red(self):
        tree = TreeSet()
        for _ in (1, 2, 4, 3, 5, 6):
            tree.add(_)
        self.assertTrue(tree.is_valid())
        tree.root.color = Color.RED
        self.assertFalse(tree.root.is_valid())

    def test_black(self):
        tree = TreeSet()
        for _ in (1, 2, 4, 3, 5, 6):
            tree.add(_)
        self.assertTrue(tree.is_valid())
        tree.root.child[1].color = Color.BLACK
        self.assertFalse(tree.root.is_valid())


class TestDictTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = TreeDict()
        for i in range(1, 8):
            self.tree[i] = 2 * i

    def test_init(self):
        self.assertEqual(3, self.tree.black_height())
        self.assertEqual(3, self.tree.height())
        self.assertEqual(4, self.tree.root.key)
        self.assertTrue(self.tree.is_valid())

    def test_get(self):
        self.assertEqual(12, self.tree[6])

    def test_set(self):
        self.tree[6] = 18
        self.assertEqual(18, self.tree[6])
        self.assertTrue(self.tree.is_valid())

    def test_del(self):
        del self.tree[4]
        self.assertEqual(2, self.tree.black_height())
        self.assertEqual(3, self.tree.height())
        self.assertEqual(3, self.tree.root.key)
        self.assertTrue(self.tree.is_valid())


class Load(unittest.TestCase):
    def test_set(self):
        trees = (TreeSet(range(i)) for i in range(127))
        self.assertTrue(all(len(t) == i for i, t in enumerate(trees)))
        self.assertTrue(all(t.is_valid() for t in trees))

    def test_dict(self):
        trees = (TreeDict({j: 2 * j for j in range(i)}) for i in range(127))
        self.assertTrue(all(len(t) == i for i, t in enumerate(trees)))
        self.assertTrue(all(t.is_valid() for t in trees))

    def test_dict_gen(self):
        trees = (TreeDict((j, 2 * j) for j in range(i)) for i in range(127))
        self.assertTrue(all(len(t) == i for i, t in enumerate(trees)))
        self.assertTrue(all(t.is_valid() for t in trees))


if __name__ == '__main__':
    unittest.main()
