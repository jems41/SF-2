"""
Deterministic Quicksort:
1. find pivot & partition O(n)
2. recursively sort left O(1) # function call itself is constant
3. recursivelly sort right O(1)

[1, 2, 3, 4, 5, 6, 7, 8, 9, ...]
    <       [ ]         >

Best case scenario: O(nlogn)
                [n]                 O(n)
               /   \
          ~[n/2]    ~[n/2]          O(n)
          /   \      /    \
     ~[n/4] ~[n/4] ~[n/4] ~[n/4]    O(n)

Height of the tree: O(logn)

Worst case scenario: O(n^2)
                [n]                 O(n)
               /   \
          ~[n-1]    ~[0]            O(n)
          /   \      /   \
     ~[n-2] ~[0]  ~[0]  ~[0]        O(n)

Height of the tree: O(n)
"""