# LeetCode精讲(0706)：设计哈希映射(Python)

## 题目内容

不使用任何内建的哈希表库设计一个哈希映射

具体地说，你的设计应该包含以下的功能

* put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。
* get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。
* remove(key)：如果映射中存在这个键，删除这个数值对。

**示例：**

```
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // 返回 1
hashMap.get(3);            // 返回 -1 (未找到)
hashMap.put(2, 1);         // 更新已有的值
hashMap.get(2);            // 返回 1 
hashMap.remove(2);         // 删除键为2的数据
hashMap.get(2);            // 返回 -1 (未找到) 
```

**注意：**

* 所有的值都在 [0, 1000000]的范围内。
* 操作的总数目在[1, 10000]范围内。
* 不要使用内建的哈希库。

> 来源：力扣（LeetCode）
> 
> 链接：https://leetcode-cn.com/problems/design-hashmap

## 解法效率

| 解法           | 时间复杂度                                                   | 空间复杂度 | 执行用时       |
| -------------- | ------------------------------------------------------------ | ---------- | -------------- |
| Ans 1 (Python) | 查询：$O(\frac{N}{K})$；添加：；$O(\frac{N}{K})$删除：$O(\frac{N}{K})$ | $O(N+K)$   | 超出时间限制   |
| Ans 2 (Python) | 查询：$O(\frac{N}{K})$；添加：；$O(\frac{N}{K})$删除：$O(\frac{N}{K})$ | $O(N+K)$   | 260ms (73.95%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

### 解法一（使用链表作为存储空间）

> **【思路】**
>
> 首先，我们使用取模运算作为哈希方法， 并选择较大的质数作为除数(KeyRange)，以降低哈希碰撞的概率，在下例中我们使用1000以内最大的质数997；
>
> 然后，我们定义数组array作为存储空间，通过哈希方法计算键(key)的模，即在array数组中存储该键的下标。
>
> 接着，我们使用链表(Bucket)来存储模相同的数据。
>
> 具体实现如下：

```python
class MyHashMap:

    def __init__(self):
        self.keyRange = 997
        self.array = [Bucket() for _ in range(997)]

    def _hash(self, key: int):
        return key % self.keyRange

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        self.array[idx].insert(key, value)

    def get(self, key: int) -> int:
        idx = self._hash(key)
        return self.array[idx].get(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.array[idx].remove(key)


class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + "{" + "{}".format(self.gatherAttrs()) + "}"


class Bucket:

    def __init__(self):
        self.root = Node(-1, None)

    def insert(self, key, val):
        node = self.root
        last = self.root
        while node:
            if node.key == key:
                node.val = val
                break
            last = node
            node = node.next
        else:
            last.next = Node(key, val)

    def get(self, key):
        node = self.root
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key):
        node = self.root
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                break
```

### 解法二（使用数组作为存储空间）

> **【思路】**
>
> 我们改用数组作为存储空间，来存储模相同的数据。
>
> 具体实现如下：

```python
class MyHashMap:

    def __init__(self):
        self.keyRange = 997
        self.array = [Bucket() for _ in range(997)]

    def _hash(self, key: int):
        return key % self.keyRange

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        self.array[idx].insert(key, value)

    def get(self, key: int) -> int:
        idx = self._hash(key)
        return self.array[idx].get(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.array[idx].remove(key)


class Bucket:

    def __init__(self):
        self.array = []

    def insert(self, key, value):
        for i, kv in enumerate(self.array):
            if kv[0] == key:
                self.array[i] = (key, value)
                break
        else:
            self.array.append((key, value))

    def get(self, key):
        for (k, v) in self.array:
            if k == key:
                return v
        else:
            return -1

    def remove(self, key):
        for i, kv in enumerate(self.array):
            if kv[0] == key:
                del self.array[i]
```