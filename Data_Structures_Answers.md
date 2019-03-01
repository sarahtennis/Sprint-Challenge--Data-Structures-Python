Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
O(n + n) --> O(n), linear runtime. Runs recursion method once for each node and later loops through each node in stack

2. What is the space complexity of your `depth_first_for_each` function?
O(n), linear space. Appends to list for each node.

3. What is the runtime complexity of your `breadth_first_for_each` method?
O(n), linear time. Runs while loop for each node until queue is empty.

4. What is the space complexity of your `breadth_first_for_each` method?
O(n), linear space. Queue never has all n elements at once, but space approaches linear.


5. What is the runtime complexity of the provided code in `names.py`?
O(n * m) --> O(n^2), quadratic time where n=length of first list, m=length of second list (n^2 since same length)
6. What is the space complexity of the provided code in `names.py`?
O(n + m + d) --> O(n), linear space where n=elements in first list, m=elements in second list, d=duplicates

7. What is the runtime complexity of your optimized code in `names.py`?
O(n + m) --> O(n), linear time where n=elements in first list and m=elements in second list

8. What is the space complexity of your optimized code in `names.py`?
O(n + d) --> O(n), linear space where n=elements in first list and d=duplicates between lists
