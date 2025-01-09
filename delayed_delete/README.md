# Delayed Delete
You are building a text editor feature that needs to handle a special type of undo operation. The editor maintains a string and supports a unique 'delayed delete' operation where 
characters can be marked for deletion but are only removed after a specific delay. You need to implement a function that porcesses a sequence of delayed delete operations and returns the final string. 
Each delete operation consists of a position index and a dealy time (in steps). A character is only deleted when its delay counter reaches zero, and the counter decreases by 1 after each operation
is processed. If multiple characters are ready to be deleted in the same step, they are removed from right to left.

### Example 1
**Input** : input_string - 'abcdef', operations = [[0,2],[1,1],[2,1]]

**Output** : def

**Explanation** : After first step, no deletion (all delays>0), After second step, 'b' and 'c' are deleted (delays become 0). After third step, 'a' is deleted (delay become 0)
