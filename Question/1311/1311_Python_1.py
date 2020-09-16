import collections
from typing import List


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


if __name__ == "__main__":
    print(Solution().watchedVideosByFriends(watchedVideos=[["A", "B"], ["C"], ["B", "C"], ["D"]], friends=[[1, 2], [0, 3], [0, 3], [1, 2]], id=0,
                                            level=1))  # ["B","C"]
    print(Solution().watchedVideosByFriends(watchedVideos=[["A", "B"], ["C"], ["B", "C"], ["D"]], friends=[[1, 2], [0, 3], [0, 3], [1, 2]], id=0,
                                            level=2))  # ["D"]
