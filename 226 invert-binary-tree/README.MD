
URL: https://leetcode.com/problems/invert-binary-tree/

# IDEA
Given a binary tree invert every child of every node

# Solution
I used a recursive method that would store the inverted version of the right 
child as a temp variable and then set right child to be the inverted version
of the left child and then set left child to be the temp variable.