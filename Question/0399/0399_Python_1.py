from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        params = set(p1 for p1, p2 in equations) | set(p2 for p1, p2 in equations)
        size = len(equations)

        # 构造图
        graph = {param: {} for param in params}
        for i in range(size):
            (x, y), value = equations[i], values[i]
            graph[x][y] = value
            graph[y][x] = 1 / value

        def dfs(n1, n3, visited, now=1):
            for n2 in graph[n1]:
                if n2 not in visited:
                    if n2 == n3:
                        return now * graph[n1][n2]
                    else:
                        v = dfs(n2, n3, visited=visited | {n2}, now=now * graph[n1][n2])
                        if v != -1:
                            return v
            return -1

        # 深度优先搜索解题
        ans = []
        for x, y in queries:
            if x not in graph or y not in graph:
                ans.append(-1)
            elif x == y:
                ans.append(1)
            else:
                ans.append(dfs(x, y, visited={x}))

        return ans


if __name__ == "__main__":
    # [6.0, 0.5, -1.0, 1.0, -1.0 ]
    print(Solution().calcEquation(
        equations=[["a", "b"], ["b", "c"]],
        values=[2.0, 3.0],
        queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    ))

    # [3.75000,0.40000,5.00000,0.20000]
    print(Solution().calcEquation(
        equations=[["a", "b"], ["b", "c"], ["bc", "cd"]],
        values=[1.5, 2.5, 5.0],
        queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    ))

    # [0.50000,2.00000,-1.00000,-1.00000]
    print(Solution().calcEquation(
        equations=[["a", "b"]],
        values=[0.5],
        queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    ))
