# LeetCode题解(1601)：最多可达成的换楼请求数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-number-of-achievable-transfer-requests/)（困难）

标签：贪心算法、递归、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 144ms (93%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0

        count_from = [0] * n
        count_to = [0] * n
        now_requests = []

        # 数量统计
        for request in requests:
            if request[0] == request[1]:
                ans += 1
            else:
                now_requests.append((request[0], request[1]))
                count_from[request[0]] += 1
                count_to[request[1]] += 1

        # 不断筛选
        while True:
            # 判断是否剩余请求均可满足
            for i in range(n):
                if count_from[i] != count_to[i]:
                    break
            else:
                return ans + len(now_requests)

            # 过滤绝对不可能完成的请求
            new_requests = []
            for request in now_requests:
                if count_from[request[1]] == 0:
                    count_to[request[1]] -= 1
                    count_from[request[0]] -= 1
                else:
                    new_requests.append(request)

            # 处理过滤了不可能完成的请求的情况
            if len(new_requests) != len(now_requests):
                now_requests = new_requests
                continue

            else:
                # 递归处理可选择的不可能完成的请求
                for i in range(n):
                    if count_from[i] < count_to[i]:
                        maybe_lst = []
                        for request in now_requests:
                            if request[1] == i:
                                maybe_lst.append(request)

                        part_max = 0
                        for maybe in maybe_lst:
                            now_requests.remove(maybe)
                            part_max = max(part_max, self.maximumRequests(n, now_requests))
                            now_requests.append(maybe)

                        return ans + part_max
```