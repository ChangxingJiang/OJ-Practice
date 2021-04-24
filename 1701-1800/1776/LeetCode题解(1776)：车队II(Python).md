# LeetCode题解(1776)：车队II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/car-fleet-ii/)（困难）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 816ms (34.04%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
import collections


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        size = len(cars)

        ans = [0] * size

        # 当前车速度变量：group_speed[0]=时间结点,group_speed[1]=时间结点的位置,group_speed[2]=时间结点后的速度
        group_speed = collections.deque()

        for i in range(size - 1, -1, -1):
            # print(group_speed, "<-", (cars[i]))

            position1, speed1 = cars[i]

            # 当前车就是最后一辆车的情况
            if not group_speed:
                ans[i] = -1
                group_speed = collections.deque([[0, position1, speed1]])

            # 当前车无法追上前面的车队的情况
            elif group_speed[-1][2] >= speed1:
                ans[i] = -1
                group_speed = collections.deque([[0, position1, speed1]])

            # 当前车可以追上前面的车的情况
            # 在没有追上前面的车之前，当前车一直保持出发的速度（前面的车在这段时间怎么变化速度并不影响后车）
            else:
                while len(group_speed) > 0:
                    # 前面还有大于等于1次速度变化
                    if len(group_speed) >= 2:
                        # 在下一次速度变化前就可以追上前车
                        if position1 + group_speed[1][0] * speed1 > group_speed[1][1]:
                            time2, position2, speed2 = group_speed[0]  # 追击段前车信息
                            position3 = position1 + time2 * speed1  # 追击前后车位置
                            diff_speed = speed1 - speed2  # 速度差
                            diff_distance = position2 - position3  # 距离差
                            time = diff_distance / diff_speed  # 追击时间
                            new_time = time2 + time  # 追击时间
                            new_position = position2 + time * speed2  # 追击位置

                            # 更新当前速度信息
                            ans[i] = new_time
                            group_speed[0][0] = new_time
                            group_speed[0][1] = new_position
                            group_speed.appendleft([0, position1, speed1])
                            break

                        # 在下次速度变化时追上前车
                        elif position1 + group_speed[1][0] * speed1 == group_speed[1][1]:
                            ans[i] = group_speed[1][0]
                            group_speed.popleft()
                            group_speed.appendleft([0, position1, speed1])
                            break

                        # 在下次速度变化前追不上前车
                        else:
                            group_speed.popleft()

                    # 前面不再有速度变化
                    elif len(group_speed) == 1:
                        # 更新当前速度信息
                        time2, position2, speed2 = group_speed[0]  # 追击段前车信息
                        position3 = position1 + time2 * speed1  # 追击前后车位置
                        diff_speed = speed1 - speed2  # 速度差
                        diff_distance = position2 - position3  # 距离差
                        time = diff_distance / diff_speed  # 追击时间
                        new_time = time2 + time  # 追击时间
                        new_position = position2 + time * speed2  # 追击位置

                        # 更新当前速度信息
                        ans[i] = new_time
                        group_speed[0][0] = new_time
                        group_speed[0][1] = new_position
                        group_speed.appendleft([0, position1, speed1])
                        break

        return ans
```

