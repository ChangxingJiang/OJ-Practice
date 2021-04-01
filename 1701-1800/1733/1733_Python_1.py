from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        need_friends = set()  # 需要学习语言才能交流的好友列表

        languages = [set(language) for language in languages]

        for u, v in friendships:
            if not languages[u - 1] & languages[v - 1]:
                need_friends.add(u)
                need_friends.add(v)

        language_knows_num = [0] * n  # 每种语言在需要学习语言的好友中已学习的数量
        for friend in need_friends:
            for i in languages[friend - 1]:
                language_knows_num[i - 1] += 1

        return len(need_friends) - max(language_knows_num)


if __name__ == "__main__":
    # 1
    print(Solution().minimumTeachings(n=2, languages=[[1], [2], [1, 2]], friendships=[[1, 2], [1, 3], [2, 3]]))

    # 2
    print(Solution().minimumTeachings(n=3, languages=[[2], [1, 3], [1, 2], [3]],
                                      friendships=[[1, 4], [1, 2], [3, 4], [2, 3]]))
