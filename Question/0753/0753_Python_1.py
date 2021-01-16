class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        visited = set()

        def dfs(s1):
            visited.add(s1)
            for v in range(k):
                s2 = s1[1:] + str(v)
                if s2 not in visited:
                    dfs(s2)
            stack.append(s1[0])

        # 处理其他进制的情况
        stack = ["0" * (n - 1)]
        dfs("0" * n)
        return "".join(stack[::-1])


if __name__ == "__main__":
    print(Solution().crackSafe(1, 1))  # 0
    print(Solution().crackSafe(1, 2))  # 01
    print(Solution().crackSafe(2, 2))  # 00110
    print(Solution().crackSafe(3, 2))  # 0011101000
