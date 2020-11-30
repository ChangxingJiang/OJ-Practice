# LeetCode题解(面试16.18)：模式匹配(Python)

题目：[原题链接](https://leetcode-cn.com/problems/pattern-matching-lcci/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 416ms (13.98%) |
| Ans 2 (Python) | $O(N^2)$   | $O(N)$     | 44ms (65.68%)  |
| Ans 3 (Python) |            |            |                |

解法一（暴力解法）：

```python
class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        size1, size2 = len(pattern), len(value)

        # 处理value为空的特殊情况
        if size2 == 0:
            return size1 == 1

        for i1 in range(size2 + 1):
            p1, s1 = pattern[0], value[:i1]  # 模式值、对应的字符串值
            j1 = 1  # 当前模式中的位置
            i2 = i1  # 当前字符串中的位置

            # 连续匹配当前值
            right = True
            while j1 < size1 and i2 < size2 and pattern[j1] == p1:
                if value[i2:i2 + i1] == s1:
                    j1 += 1
                    i2 += i1
                else:
                    right = False
                    break

            # 处理已经匹配完成的情况
            if j1 >= size1 or i2 >= size2:
                if p1 not in pattern[j1:] and i2 == size2 and right:
                    return True
                else:
                    continue

            # 未能匹配则跳过
            if not right:
                continue

            for i3 in range(i2 + 1, size2 + 1):
                p2, s2 = pattern[j1], value[i2:i3]

                j2 = j1 + 1
                i4 = i3
                # 检查当前情况是否正确
                right = True
                while j2 < size1 and i4 <= size2:
                    if pattern[j2] == p1:
                        if i1 > 0:
                            if value[i4:i4 + i1] == s1:
                                j2 += 1
                                i4 += i1
                            else:
                                right = False
                                break
                        else:
                            j2 += 1
                    else:
                        if i3 - i2 > 0:
                            if value[i4:i4 + (i3 - i2)] == s2:
                                j2 += 1
                                i4 += (i3 - i2)
                            else:
                                right = False
                                break
                        else:
                            j2 += 1

                # print(right, "第1个:", s1, "第2个:", s2, "(", j2, "/", size1, ")", "(", i4, "/", size2, ")")

                # 如果匹配成功则返回
                if right and j2 == size1 and i4 == size2:
                    return True

        return False
```

解法二：

```python
class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        size1, size2 = len(pattern), len(value)

        # 处理value为空的特殊情况
        if size2 == 0:
            return size1 == 1

        count = collections.Counter(pattern)
        count1, count2 = count["a"], count["b"]

        # 如果有一个模式的出现频数为1，则令该模式为整串即可
        if count1 == 1 or count2 == 1:
            return True

        # 处理只出现一种模式的情况
        if count1 == 0 or count2 == 0:
            if size2 % (count1 + count2) != 0:
                return False
            p = size2 // (count1 + count2)
            for l in range(0, size2 - p, p):
                if value[l:l + p] != value[l + p:l + 2 * p]:
                    return False
            return True

        # 处理两种模式均有出现的情况
        for l1 in range(size2 // count1 + 1):
            if (size2 - count1 * l1) % count2 != 0:
                continue
            l2 = (size2 - count1 * l1) // count2
            a, b = "", ""
            j1, j2 = 0, 0
            while j1 < size1 and j2 < size2:
                if pattern[j1] == "a":
                    if j2 + l1 > size2:
                        break
                    ch = value[j2:j2 + l1]
                    j2 += l1
                    if a == "":
                        a = ch
                    else:
                        if a != ch:
                            break
                else:
                    if j2 + l2 > size2:
                        break
                    ch = value[j2:j2 + l2]
                    j2 += l2
                    if b == "":
                        b = ch
                    else:
                        if b != ch:
                            break
                j1 += 1
            else:
                return True

        return False
```