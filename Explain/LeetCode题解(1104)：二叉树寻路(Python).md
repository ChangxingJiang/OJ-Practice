# LeetCode题解(1104)：在Z字型完全二叉树中寻找到指定叶节点的路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree/)（中等）

标签：树、二叉树、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 44ms (48.52%) |
| Ans 2 (Python) | $O(logN)$  | $O(1)$     | 44ms (48.52%) |
| Ans 3 (Python) | $O(logN)$  | $O(1)$     | 40ms (73.70%) |

解法一：

```python
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 生成2的倍数数列
        lst = [1]
        while lst[-1] <= label:
            lst.append(lst[-1] * 2)

        # 计算当前点的真实坐标
        if len(lst) % 2 == 1:
            idx = lst[-2] + lst[-1] - label - 1
            reverse = True
            most_val = lst[-1]
        else:
            idx = label
            reverse = False
            most_val = lst[-1]

        # 生成结果路径
        ans = []
        while idx > 1:
            most_val //= 2
            if reverse:
                ans.append(3 * most_val - idx - 1)
            else:
                ans.append(idx)
            idx //= 2
            reverse = not reverse
        ans.append(1)

        return list(reversed(ans))
```

解法二：

```python
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 生成2的倍数数列
        num_lst = [1]
        while num_lst[-1] <= label:
            num_lst.append(num_lst[-1] * 2)

        # 计算当前点的真实坐标
        if len(num_lst) % 2 == 1:
            now_idx = num_lst[-2] + num_lst[-1] - label - 1
        else:
            now_idx = label

        # 生成坐标列表
        idx_lst = []
        while now_idx > 1:
            idx_lst.append(now_idx)
            now_idx //= 2
        idx_lst.append(1)
        idx_lst.reverse()

        ans = []
        reverse = False
        for i in range(len(idx_lst)):
            idx = idx_lst[i]
            num1 = num_lst[i]
            num2 = num_lst[i + 1]
            if reverse:
                ans.append(num1 + num2 - idx - 1)
            else:
                ans.append(idx)
            reverse = not reverse

        return ans
```

解法三（使用math模块）：

```python
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = []
        while label > 1:
            print(label)
            ans.append(label)
            last_line_num = int(math.log2(label))  # 上一行的行数
            last_line_right = pow(2, last_line_num - 1)  # 当前行最左侧的数在未Z字型转换的完全二叉树中的坐标
            label = 3 * last_line_right - label // 2 - 1

        ans.append(1)
        return ans[::-1]
```

