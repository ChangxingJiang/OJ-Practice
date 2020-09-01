# LeetCode题解(0076)：找出字符串S中包含字符串T中所有字符的最小子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-window-substring/)（困难）

标签：字符串、哈希表、双指针、滑动窗口

| 解法           | 时间复杂度                       | 空间复杂度                | 执行用时       |
| -------------- | -------------------------------- | ------------------------- | -------------- |
| Ans 1 (Python) | $O(C×(S+T))$ : 其中C为字符集数量 | $O(C)$: 其中C为字符集数量 | 652ms (13.91%) |
| Ans 2 (Python) | $O(S+T)$                         | $O(C)$: 其中C为字符集数量 | 84ms (94.88%)  |
| Ans 3 (Python) |                                  |                           |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（朴素的滑动窗口）：

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contain():
            for a in aim:
                if a not in count or count[a] < aim[a]:
                    return False
            return True

        N = len(s)
        aim = collections.Counter(t)

        ans = None

        left = right = 0  # 窗口左侧和窗口右侧的坐标
        count = collections.Counter()  # 当前窗口内各所需字母数量
        while right < N:
            ch = s[right]
            if ch in aim:  # 更新窗口内字母数量
                count[ch] += 1
            while left <= right and (s[left] not in aim or count[s[left]] > aim[s[left]]):  # 更新窗口左侧边缘位置
                if count[s[left]] > aim[s[left]]:
                    count[s[left]] -= 1
                left += 1

            right += 1
            # print(left, right, "[", ch, "]", "->", count)

            # 判断当前结果是否为最小覆盖子串
            if contain():
                if not ans or right - left - 1 < len(ans):
                    ans = s[left:right]

        return ans if ans else ""
```

解法二（优化滑动窗口）：

1. 使用剩余未覆盖字母数替代字典比较

2. 增加最终结果长度的临时变量
3. 将目标字典和窗口内数量字典合并为一个
4. 减少无意义的当前窗口是否为结果的判断
5. 直接存储结果字符串的起始坐标
6. 用collections.defaultdict替代collections.Counter

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        surplus = len(t)  # 当前剩余尚未覆盖的字母数
        count = collections.Counter(t)

        ans_len, ans = float("inf"), ""

        left = 0  # 窗口左侧和窗口右侧的坐标
        for right, ch in enumerate(s):
            change = False  # 是否有可能出现答案的变化（达成覆盖|移动左侧边缘)

            # 更新窗口内字母数量
            if ch in count:
                count[ch] -= 1
                if count[ch] >= 0:
                    surplus -= 1
                    change = True

            # 更新窗口左侧边缘位置
            while left <= right and (s[left] not in count or count[s[left]] < 0):
                if s[left] in count:
                    count[s[left]] += 1
                left += 1
                change = True

            # 判断当前结果是否为最小覆盖子串
            if change and surplus == 0:
                if right - left < ans_len:
                    ans = s[left:right + 1]
                    ans_len = right - left

        return ans
```