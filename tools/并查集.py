"""DSU (Disjoint Set Union) 并查集

1. 包含路径压缩功能（在find的过程中直接进行路径压缩）
2. 包含依据节点数量选择领导者的功能（在union中依据子节点数量选择领导者）

函数说明：
    DSU(n) 构造并查集实例：n=并查集中元素的数量
    find(i) 查询元素i所在集合的代表（这个操作也可以用来判断两个元素是否位于同一个集合中）
    union(i,j) 合并元素i和元素j所在的集合，要求元素i和元素j所在集合不想交，如果相交则不合并

其他类说明：
    DDSU 可以适用于有向图的并查集，union函数的含义为元素i指向元素j
"""


class DSU:
    def __init__(self, n):
        self.array = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i):
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if self.size[i] >= self.size[j]:
            self.array[j] = i
            self.size[i] += self.size[j]
        else:
            self.array[i] = j
            self.size[j] += self.size[i]


class DDSU:
    def __init__(self, n):
        self.array = [i for i in range(n)]

    def find(self, i):
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i, j):
        self.array[self.find(j)] = self.find(i)
