# LeetCode题解(面试03.06)：动物收容所(Python)

题目：[原题链接](https://leetcode-cn.com/problems/animal-shelter-lcci/)（简单）

标签：设计、队列

| 解法           | 时间复杂度        | 空间复杂度 | 执行用时       |
| -------------- | ----------------- | ---------- | -------------- |
| Ans 1 (Python) | 所有方法 : $O(1)$ | $O(N)$     | 144ms (92.46%) |
| Ans 2 (Python) |                   |            |                |
| Ans 3 (Python) |                   |            |                |

解法一（队列）：

```python
class AnimalShelf:

    def __init__(self):
        self.idx = 0
        self.cats = collections.deque([])
        self.dogs = collections.deque([])

    def enqueue(self, animal: List[int]) -> None:
        if animal[1] == 0:
            self.cats.append((self.idx, animal))
        else:
            self.dogs.append((self.idx, animal))
        self.idx += 1

    def dequeueAny(self) -> List[int]:
        if not self.cats and not self.dogs:
            return [-1, -1]
        elif not self.cats:
            return self.dogs.popleft()[1]
        elif not self.dogs:
            return self.cats.popleft()[1]
        else:
            if self.dogs[0][0] < self.cats[0][0]:
                return self.dogs.popleft()[1]
            else:
                return self.cats.popleft()[1]

    def dequeueDog(self) -> List[int]:
        if not self.dogs:
            return [-1,-1]
        else:
            return self.dogs.popleft()[1]

    def dequeueCat(self) -> List[int]:
        if not self.cats:
            return [-1, -1]
        else:
            return self.cats.popleft()[1]
```