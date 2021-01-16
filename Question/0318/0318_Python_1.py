import heapq
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words:
            return 0

        size = len(words)
        words.sort(key=lambda x: len(x), reverse=True)

        # 计算单词长度
        length = [len(word) for word in words]

        # 压缩单词状态
        stats = []
        for word in words:
            stats.append(0)
            for ch in word:
                stats[-1] |= 1 << (ord(ch) - 97)

        # 从大到小遍历
        visited = {(0, 0)}
        heap = [(-length[0] * length[0], 0, 0)]
        while len(visited) < size * size or heap:
            res, i, j = heapq.heappop(heap)
            if stats[i] & stats[j] == 0:
                return -res
            if i + 1 < size and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heapq.heappush(heap, (-length[i + 1] * length[j], i + 1, j))
            if j + 1 < size and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heapq.heappush(heap, (-length[i] * length[j + 1], i, j + 1))

        return 0


if __name__ == "__main__":
    # 16
    print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))

    # 4
    print(Solution().maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))

    # 0
    print(Solution().maxProduct(["a", "aa", "aaa", "aaaa"]))
