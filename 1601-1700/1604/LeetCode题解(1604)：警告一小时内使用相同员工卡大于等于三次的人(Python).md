# LeetCode题解(1604)：警告一小时内使用相同员工卡大于等于三次的人(Python)

题目：[原题链接](https://leetcode-cn.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/)（中等）

标签：字符串、排序、有序映射

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 204ms (100%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        # 将每个人的放到一起
        record = collections.defaultdict(list)
        for i in range(len(keyName)):
            name = keyName[i]
            time = float(keyTime[i].replace(":", "."))
            record[name].append(time)

        # 排序每个人的时间线
        for name, times in record.items():
            record[name] = list(sorted(times))

        # 检查每个人是否需要被警告
        ans = set()
        for name, times in record.items():
            now = []
            for time in times:
                now.append(time)
                if len(now) >= 3:
                    old_time = now.pop(0)
                    if 0 <= time - old_time <= 1.00000001:
                        ans.add(name)

        return list(sorted(ans))
```

