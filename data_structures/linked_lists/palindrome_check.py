
Is Palindrome: Given a Linked List, determine if it is a Palindrome. For example, the following lists are palindromes: 
A -> B -> C -> B -> A 
A -> B -> B -> A 
K -> A -> Y -> A -> K

Note: Can you do it with O(N) time and O(1) space? (Hint: Reverse a part of the list)

  Solution 1:- We can create a new list in reversed order and then compare each node. The time and space are O(n).
  Solution 2:- We can use a fast and slow pointer to get the center of the list, then reverse the second list and compare two sublists. 
               The time is O(n) and space is O(1).  
