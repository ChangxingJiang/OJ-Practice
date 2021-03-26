import collections


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N1 = len(s1)
        N2 = len(s2)
        N3 = len(s3)
        visited = set()
        queue = collections.deque([(0, 0, 0)])  # 使用双向队列实现当前分支
        while queue:
            i1, i2, i3 = queue.popleft()
            if (i1, i2) not in visited:
                visited.add((i1, i2))
                if i3 == N3:
                    return i1 == N1 and i2 == N2
                if i1 < N1 and s1[i1] == s3[i3]:
                    queue.append((i1 + 1, i2, i3 + 1))
                if i2 < N2 and s2[i2] == s3[i3]:
                    queue.append((i1, i2 + 1, i3 + 1))
        return False


if __name__ == "__main__":
    print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))  # True
    print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))  # False
    print(Solution().isInterleave(s1="a", s2="b", s3="a"))  # False
