from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()

        ans = 0
        last = 0
        now = 0

        for clip in clips:
            if last < clip[0]:
                if now >= clip[0]:
                    last = now
                    ans += 1
                else:
                    return -1

            if now < clip[1]:
                now = clip[1]

            if now >= T:
                return ans + 1

        return -1


if __name__ == "__main__":
    print(Solution().videoStitching(clips=[[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], T=10))  # 3

    print(Solution().videoStitching(clips=[[0, 1], [1, 2]], T=5))  # -1

    print(Solution().videoStitching(
        clips=[[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3], [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4],
               [4, 5], [5, 7], [6, 9]], T=9))  # 3

    print(Solution().videoStitching(clips=[[0, 4], [2, 8]], T=5))  # 2
