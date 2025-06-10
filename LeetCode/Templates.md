# LeetCode Solution Templates 🧩 <!-- omit in toc -->
Quick templates for every major LeetCode topic -- solve **smarter**, not harder.

[**AlgoMonster flowchart**](https://algo.monster/flowchart)

- [Backtracking](#backtracking)





---



### Backtracking

Example base: [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/description/)

```
class Solution:
    def example(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        n = len(s)

        def dfs(i):
            # Case 1: record answer for each step
            # path is global, use .copy to record
            ans.append(path.copy())

            if i == n:
            # Case 2: record answer after looping 
            # the whole input string or list
                ans.append(path.copy())
                return
            
            for j in range(i, n):
            
            # condition or filter to meet
                t = s[i:j+1]
                if t == t[::-1]:
            # backtracking mechanism
                    path.append(t)
                    dfs(j+1)
                    path.pop()

        dfs(0)
        return ans
```