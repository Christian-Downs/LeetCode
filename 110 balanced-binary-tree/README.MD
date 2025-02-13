
URL: https://leetcode.com/problems/balanced-binary-tree/

# Idea
When given either nothing or a binary tree determine if the tree is balanced, that's 
when there is an equal number of child nodes for both children of all child nodes with
a max of 1 difference.

# Solution
I used a recursive method called depth that looked at each child node of a node
and looked to see how many children are present and if there is more than one
difference between the two children set a class variable of balanced to false
then after finish recursion returns the balanced variable.
