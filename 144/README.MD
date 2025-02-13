
URL: https://leetcode.com/problems/binary-tree-preorder-traversal/

# IDEA
Given a binary tree do a preorder traversal and return it as a list

# Solution
Since a preorder traversal is just do left then right all I did was 
make a recursive method that would add itself then all the items to 
the left of it and then add all the items to the right of it.