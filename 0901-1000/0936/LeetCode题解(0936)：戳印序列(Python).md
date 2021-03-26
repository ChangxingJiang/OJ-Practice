# LeetCode题解(0936)：序列能否由指定印章印成(Python)

题目：[原题链接](https://leetcode-cn.com/problems/stamping-the-sequence/)（困难）

标签：字符串、正则表达式、贪心算法

| 解法           | 时间复杂度  | 空间复杂度  | 执行用时        |
| -------------- | ----------- | ----------- | --------------- |
| Ans 1 (Python) | --          | --          | 1796ms (13.89%) |
| Ans 2 (Python) | $O(N(N-M))$ | $O(N(N-M))$ | 220ms (66.11%)  |
| Ans 3 (Python) | $O(N^2×M)$  | $O(N)$      | 100ms (94.44%)  |

解法一（朴素的正则表达式）：

```python
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        # 生成正则表达式
        S = len(stamp)
        if S == 1:
            regex = stamp
            repl = "#"
        else:
            regex = []
            for i in range(0, S):
                tmp = []
                for j in range(0, S):
                    if j != i:
                        tmp.append("[#" + stamp[j] + "]")
                    else:
                        tmp.append(stamp[j])
                regex.append("".join(tmp))
            regex = "|".join(regex)
            repl = "#" * S

        # 计算印制顺序
        ans = []
        while True:
            match = re.search(regex, target)
            if match:
                i1 = match.span()[0]
                i2 = match.span()[1]
                target = target[:i1] + repl + target[i2:]
                ans.append(i1)
            else:
                break

        # 判断印制是否成功
        if target.count("#") == len(target):
            return list(reversed(ans))
        else:
            return []
```

解法二（逆推法）：

```python
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        M, N = len(stamp), len(target)

        queue = collections.deque()  # 当前新变化的坐标
        done = [False] * N  # 完成情况

        ans = []

        # 生成完成列表
        A = []
        for i in range(N - M + 1):
            made, todo = set(), set()
            for j, sch in enumerate(stamp):
                tch = target[i + j]
                if tch == sch:
                    made.add(i + j)
                else:
                    todo.add(i + j)
            A.append((made, todo))

            if not todo:
                ans.append(i)
                for j in range(i, i + len(stamp)):
                    if not done[j]:
                        queue.append(j)
                        done[j] = True

        while queue:
            i = queue.popleft()
            for j in range(max(0, i - M - 1), min(N - M, i) + 1):
                if i in A[j][1]:
                    A[j][1].discard(i)
                    if not A[j][1]:
                        ans.append(j)
                        for m in A[j][0]:
                            if not done[m]:
                                queue.append(m)
                                done[m] = True

        if all(done):
            return ans[::-1]
        else:
            return []
```

解法三（逆推法）：

```python
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        M, N = len(stamp), len(target)
        NN, MM = "#" * N, "#" * M

        # 判断字符串是否符合目标
        def match(s):
            for m in range(M):
                ch = s[m]
                if ch != "#" and ch != stamp[m]:
                    return False
            return True

        ans = []

        # 逆推法匹配结果
        while target != NN:
            find = False
            for i in range(N - M + 1):
                tmp = target[i:i + M]
                if tmp == MM:
                    continue
                if match(tmp):
                    find = True
                    ans.append(i)
                    target = target[:i] + MM + target[i + M:]
            if not find:
                return []

        return list(reversed(ans))
```