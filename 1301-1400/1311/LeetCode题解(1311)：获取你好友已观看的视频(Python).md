# LeetCode题解(1311)：获取你好友已观看的视频(Python)

题目：[原题链接](https://leetcode-cn.com/problems/get-watched-videos-by-your-friends/)（中等）

标签：字符串、哈希表、广度优先遍历、队列

| 解法           | 时间复杂度                                                 | 空间复杂度 | 执行用时      |
| -------------- | ---------------------------------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N+M+VlogV)$ : 其中N为人数，M为好友关系总数，V为电影总数 | $O(N+V)$   | 96ms (39.85%) |
| Ans 2 (Python) | $O(N+M+VlogV)$ : 其中N为人数，M为好友关系总数，V为电影总数 | $O(N+V)$   | 92ms (52.63%) |
| Ans 3 (Python) |                                                            |            |               |

解法一：

```python
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # 计算目标好友
        visited = {id}
        now = {id}
        for _ in range(level):
            new = set()
            for i in now:
                for friend in friends[i]:
                    if friend not in visited:
                        new.add(friend)
                        visited.add(friend)
            now = new

        # 计算最终结果
        frequency = collections.Counter()
        for friend in now:
            for video in watchedVideos[friend]:
                frequency[video] += 1

        videos = list(frequency.items())
        videos.sort(key=lambda x: (x[1], x[0]))

        return [video[0] for video in videos]
```

解法二（使用队列优化解法一）：

```python
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # 计算目标好友
        visited = {id}
        queue = collections.deque([id])
        for _ in range(level):
            for i in range(len(queue)):
                now = queue.popleft()
                for friend in friends[now]:
                    if friend not in visited:
                        queue.append(friend)
                        visited.add(friend)

        # 计算最终结果
        frequency = collections.Counter()
        for friend in queue:
            for video in watchedVideos[friend]:
                frequency[video] += 1

        videos = list(frequency.items())
        videos.sort(key=lambda x: (x[1], x[0]))

        return [video[0] for video in videos]
```



