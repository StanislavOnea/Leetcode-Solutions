# Intuition
The first intuition was to iterate over queries and run a dfs/bfs on the queiries[0] to check if we can find queiries[1]. The second idea was to actaully store the dependencies for each node in a set and then only check if for queiries[0] there is queiries[1] in dpendency set.
# Approach
- First aproach: iterate over queries and for each query check if second node can be found in the path of the first.
- Second aproach: iterate over all courses (since nr of courses is max 100) and for each course store the depencies in a set. Wer are using DFS in memoization manner to be sure that the sets from dp are completely asembled wehen we are going going to update for current node.
# Complexity
- Time complexity:
First aproach: O(q * n) - where q is number of queries and n number of courses.
Second aproach: O(max(q, n)).

- Space complexity:
First aproach: O(n^2) - store the connections between courses.
Second aproach: O(n^2) - store the connections between courses and dp.

# Code
First aproach:
```python3 []
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        connections = defaultdict(list)
        for a, b in prerequisites:
            connections[a].append(b)

        res = []
        for a, b in queries:
            is_found = False
            q = deque([a])
            visited = set()

            while q:
                node = q.popleft()
                if node == b:
                    is_found = True
                    break
                visited.add(node)
                for nei in connections[node]:
                    if nei not in visited:
                        q.append(nei)
            res.append(is_found)

        return res
```

Second aproach:
```python3 []
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        connections = defaultdict(list)
        for a, b in prerequisites:
            connections[a].append(b)

        dp = [set() for i in range(numCourses)]
        def dfs(course):
            for neighbor in connections[course]:
                if neighbor not in dp[course]:
                    dp[course].add(neighbor)
                    dp[course].update(dfs(neighbor))
            
            return dp[course]

        for i in range(numCourses):
            dp[i] = dfs(i)

        res = []
        for a, b in queries:
            if b in dp[a]:
                res.append(True)
            else:
                res.append(False)

        return res

```
