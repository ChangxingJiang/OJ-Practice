import collections


class AllOne:
    def __init__(self):
        self.buckets = [set()]
        self.count = collections.Counter()
        self.max_idx = 0
        self.min_idx = 0

    def inc(self, key: str) -> None:
        # 移除之前的频数
        idx = self.count[key]
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)

        # 更新最小值
        self.min_idx = min(self.min_idx, idx)
        if len(self.buckets[idx]) == 0 and self.min_idx == idx:
            self.min_idx += 1

        # 插入新的频数
        idx += 1
        if len(self.buckets) <= idx:
            self.buckets.append(set())
        self.buckets[idx].add(key)

        # 更新位置记录
        self.count[key] += 1

        # 更新最大值
        self.max_idx = max(self.max_idx, idx)

    def dec(self, key: str) -> None:
        # 如果没有该元素，不做任何事
        if self.count[key] == 0:
            return

        # 移除之前的频数
        idx = self.count[key]
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)

        # 更新最大值
        if len(self.buckets[idx]) == 0 and self.max_idx == idx:
            self.max_idx -= 1

        # 插入新的频数
        idx -= 1
        if idx > 0:
            self.buckets[idx].add(key)

        # 更新位置记录
        self.count[key] -= 1
        if self.count[key] == 0:
            del self.count[key]

        # 更新最小值（未实现真正的O(1)）
        if len(self.buckets[idx + 1]) == 0 and self.min_idx == idx + 1:
            self.min_idx -= 1
        if self.min_idx == 0 and self.max_idx >= 1:
            for i in range(1, self.max_idx + 1):
                if len(self.buckets[i]) > 0:
                    self.min_idx = i
                    break

    def getMaxKey(self) -> str:
        if self.max_idx > 0:
            res = self.buckets[self.max_idx].pop()
            self.buckets[self.max_idx].add(res)
            return res
        else:
            return ""

    def getMinKey(self) -> str:
        if self.min_idx > 0:
            res = self.buckets[self.min_idx].pop()
            self.buckets[self.min_idx].add(res)
            return res
        else:
            return ""


if __name__ == "__main__":
    obj = AllOne()
    obj.inc("hello")
    obj.inc("hello")
    print(obj.getMaxKey())  # hello
    print(obj.getMinKey())  # hello
    obj.inc("leet")
    print(obj.getMaxKey())  # hello
    print(obj.getMinKey())  # leet
