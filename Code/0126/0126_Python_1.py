from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        N = len(beginWord)

        # 比较两个字符串是否可以通过一次转换获得
        def check_transform(str1, str2):
            differences = 0
            for i in range(N):
                if str1[i] != str2[i]:
                    differences += 1
                    if differences >= 2:
                        return False
            return differences == 1

        # 处理目标词不存在于词典的情况
        if endWord not in wordList:
            return []

        visited = set()
        now_paths = [(beginWord,)]  # 当前路径
        ans = []
        while now_paths:
            now_visited = set()
            next_paths = []
            for path in now_paths:
                now = path[-1]
                for word in wordList:
                    if word not in visited and check_transform(now, word):
                        if word == endWord:
                            ans.append(list(path + (word,)))
                        else:
                            now_visited.add(word)
                            next_paths.append(path + (word,))
            now_paths = next_paths
            visited.update(now_visited)
            if ans:
                break
        return ans


if __name__ == "__main__":
    # [
    #   ["hit","hot","dot","dog","cog"],
    #   ["hit","hot","lot","log","cog"]
    # ]
    print(Solution().findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))

    # []
    print(Solution().findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]))

    # []
    print(Solution().findLadders(beginWord="hot", endWord="cog", wordList=["hot", "dog"]))

    # [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]
    print(Solution().findLadders(beginWord="red", endWord="tax", wordList=["ted","tex","red","tax","tad","den","rex","pee"]))
