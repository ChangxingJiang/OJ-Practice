# LeetCode题解(1177)：通过替换字母能够构建的回文串检测(Python)

题目：[原题链接](https://leetcode-cn.com/problems/can-make-palindrome-from-substring/)（中等）

标签：字符串、数组、位运算

| 解法           | 时间复杂度                                                  | 空间复杂度 | 执行用时        |
| -------------- | ----------------------------------------------------------- | ---------- | --------------- |
| Ans 1 (Python) | $O(Q×N)$ : 其中Q为queries长度，N为query包含字符串的平均长度 | $O(1)$     | 超出时间限制    |
| Ans 2 (Python) | $O(Q+N)$ : 其中Q为queries长度，N为query包含字符串的平均长度 | $O(N)$     | 2628ms (40.63%) |
| Ans 3 (Python) | $O(Q+N)$ : 其中Q为queries长度，N为query包含字符串的平均长度 | $O(N)$     | 1600ms (97.92%) |

解法一（暴力解法）：

```python
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        ans = []
        for left, right, k in queries:
            differ = set()
            for i in range(left, right + 1):
                if s[i] in differ:
                    differ.remove(s[i])
                else:
                    differ.add(s[i])
            ans.append(len(differ) // 2 <= k)
        return ans
```

解法二（前缀和思路）：

```python
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        # 生成s中每一个位置的前缀字母情况
        nums = [0] * 26
        lst = [nums.copy()]
        for ch in s:
            nums[ord(ch) - 97] += 1
            lst.append(nums.copy())

        # 遍历计算每一个query是否为回文串
        ans = []
        for left, right, k in queries:
            differ = 0
            left_nums = lst[left]
            right_nums = lst[right + 1]
            for i in range(26):
                if (right_nums[i] - left_nums[i]) % 2 == 1:
                    differ += 1
            # print(left, right, k, differ, left_nums, right_nums)
            ans.append(differ // 2 <= k)

        return ans
```

解法三（只记录前缀字母的奇偶情况）：

```python
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        # 使用二进制数记录每一个位置的前缀字母的奇偶情况
        lst = [0]
        for i, ch in enumerate(s):
            # (1 << (ord(ch) - 97)) 当前字母在二进制数中的位置
            # lst[i] ^ (1 << (ord(ch) - 97)) 如果当前字母为奇数(1)则改为(0)，反之则改为(1)
            lst.append(lst[i] ^ (1 << (ord(ch) - 97)))

        # 遍历计算每一个query是否为回文串
        ans = []
        for left, right, k in queries:
            # lst[left] 左侧位置前缀字母的奇偶情况
            # lst[right + 1] 右侧位置前缀字母的奇偶情况
            # lst[left] ^ lst[right + 1] 左右侧位置前缀字母奇偶情况差异
            differ = bin(lst[left] ^ lst[right + 1]).count("1")
            ans.append(differ // 2 <= k)
        return ans
```