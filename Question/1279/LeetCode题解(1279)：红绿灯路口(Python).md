# LeetCode题解(1279)：红绿灯路口(Python)

题目：[原题链接](https://leetcode-cn.com/problems/traffic-light-controlled-intersection/)（简单）

标签：多线程

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 52ms (88.89%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
import threading

class TrafficLight:
    def __init__(self):
        self.lock = threading.Lock()
        self.now = 1

    def carArrived(
            self,
            carId: int,  # ID of the car
            roadId: int,  # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
            direction: int,  # Direction of the car
            turnGreen: 'Callable[[], None]',  # Use turnGreen() to turn light to green on current road
            crossCar: 'Callable[[], None]'  # Use crossCar() to make car cross the intersection
    ) -> None:
        self.lock.acquire()
        if self.now == roadId:
            crossCar()
        else:
            self.now = roadId
            turnGreen()
            crossCar()
        self.lock.release()
```