import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**9)


BST: TypeAlias= Union["BSTNode", None]

@dataclass
class BSTNode:
    val: Any 
    left: BST 
    right: BST 

@dataclass(frozen=True)
class BSTWithComesBefore:
    comes_before:Callable[[Any,Any],bool]
    tree: BST



def same_value(comes_before: Callable[[Any, Any], bool], val1: Any, val2: Any) -> bool:
    return not comes_before(val1, val2) and not comes_before(val2, val1)

#checks if "val" is in bst 
def lookup(bst: BSTWithComesBefore, val:Any)->bool:
    
    def helper(tree:BST, val:Any)->bool:
        if tree is None:
            return False
        
        if same_value(bst.comes_before, val, tree.val):
            return True 
        elif bst.comes_before(tree.val, val):
             return helper(tree.right, val)
        else: 
            return helper(tree.left, val)
    
    return helper(bst.tree, val)            

#inserts "val" into bst 
def insert(bst: BSTWithComesBefore, val:Any)->BSTWithComesBefore:
    def helper(tree:BST, val:Any)->BST:
        if tree is None:
            return BSTNode(val, None, None)
        if same_value(bst.comes_before, val, tree.val):
            return tree 
        elif bst.comes_before(tree.val, val):
            tree.right= helper(tree.right, val)
            return tree 
        else:
            tree.left= helper(tree.left, val)
            return tree 
    new_tree= helper(bst.tree, val)
    return BSTWithComesBefore(bst.comes_before, new_tree)
        
#helper function that finds min value in "tree"
def find_min(tree:BST)->Any:
    if tree is None:
        return None 
    
    if tree.left is None:
        return tree.val
    return find_min(tree.left)

#Deletes "val" in bst 
def delete(bst: BSTWithComesBefore, val:Any)->BSTWithComesBefore:
    def helper(tree:BST, val:Any)->BST:
        if tree is None:
            return None 
        if bst.comes_before(val, tree.val):
            tree.left = helper(tree.left, val)
            return tree 
        
        elif bst.comes_before(tree.val, val): 
            tree.right= helper(tree.right, val)
            return tree 
        else: 
            if tree.left is None:
                return tree.right 
            
            if tree.right is None: 
                return tree.left
            
            new_val: Any= find_min(tree.right)
            tree.val= new_val
            tree.right= helper(tree.right, new_val)
            return tree 
    new_tree= helper(bst.tree, val)
    return BSTWithComesBefore(bst.comes_before, new_tree)





