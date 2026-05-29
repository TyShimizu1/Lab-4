import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**9)
from bst import *


@dataclass
class Point2D:
 x: float
 y: float   

#gets alphebetical order 
def alphabetical(str1: str, str2: str) -> bool:
    return str1 < str2

#gets the distance between points 
def point_distance(p1: Point2D, p2: Point2D) -> bool:
    return p1.x**2 + p1.y**2 < p2.x**2 + p2.y**2

#
def reverse_ints(n1: int, n2: int) -> bool:
    return n1 > n2


class Tests(unittest.TestCase):

    def test_alphabetical_strings(self):
        bst:BSTWithComesBefore = BSTWithComesBefore(alphabetical, None)

        bst = insert(bst, "b")
        bst = insert(bst, "a")
        bst = insert(bst, "c")

        self.assertEqual(bst.tree.val, "b")
        self.assertEqual(bst.tree.left.val, "a")
        self.assertEqual(bst.tree.right.val, "c")

    def test_points_by_distance(self):
        bst = BSTWithComesBefore(point_distance, None)

        point1 = Point2D(0, 1)
        point2 = Point2D(3, 4)
        point3 = Point2D(6, 8)

        bst = insert(bst, point2)
        bst = insert(bst, point1)
        bst = insert(bst, point3)

        self.assertEqual(bst.tree.val, point2)
        self.assertEqual(bst.tree.left.val, point1)
        self.assertEqual(bst.tree.right.val, point3)

    def test_reverse_order_integers(self):
        bst = BSTWithComesBefore(reverse_ints, None)

        bst = insert(bst, 1)
        bst = insert(bst, 2)
        bst = insert(bst, 0)

        self.assertEqual(bst.tree.val, 1)
        self.assertEqual(bst.tree.left.val, 2)
        self.assertEqual(bst.tree.right.val, 0)

if __name__ == "__main__":
    unittest.main()


