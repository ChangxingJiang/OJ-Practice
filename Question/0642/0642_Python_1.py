import collections
import heapq
from typing import List


class TrieNode:
    def __init__(self, count=0):
        self.count = count
        self.word = ""
        self.next = collections.defaultdict(TrieNode)

    def insert(self, word, time):
        """将单词插入到当前节点"""
        curr = self
        for ch in word:
            curr = curr.next[ch]
        curr.word = word
        curr.count = time

    def __lt__(self, other):
        if self.count < other.count:
            return True
        elif self.count > other.count:
            return False
        return self.word > other.word

    def get_words(self):
        """搜索当前节点一下的所有单词"""
        ans, queue = list(), collections.deque([self, ])
        while queue:
            curr = queue.popleft()
            if curr.count:
                heapq.heappush(ans, curr)
                if len(ans) > 3:
                    heapq.heappop(ans)
            for node in curr.next.values():
                queue.append(node)
        ans.sort(reverse=True)
        return [node.word for node in ans]


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.curr = self.root
        self.word = ""

        # 初始化字典树
        for word, time in zip(sentences, times):
            self.root.insert(word, time)

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.curr.word = self.word
            self.curr.count += 1
            self.curr = self.root
            self.word = ""
            return []
        if c not in self.curr.next:
            self.curr = self.curr.next[c]
            self.word += c
            return []
        else:
            self.curr = self.curr.next[c]
            self.word += c
            return self.curr.get_words()


if __name__ == "__main__":
    obj = AutocompleteSystem(["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2])
    print(obj.input("i"))  # ["i love you", "island","i love leetcode"]
    print(obj.input(" "))  # ["i love you","i love leetcode"]
    print(obj.input("a"))  # []
    print(obj.input("#"))  # []
    print(obj.input("i"))  # ["i love you", "island","i love leetcode"]
    print(obj.input(" "))  # ["i love you","i love leetcode","i a"]
    print(obj.input("a"))  # ["i a"]
    print(obj.input("#"))  # []
    print(obj.input("i"))  # ["i love you","island","i a"]
    print(obj.input(" "))  # ["i love you","i a","i love leetcode"]
    print(obj.input("a"))  # ["i a"]
    print(obj.input("#"))  # []
