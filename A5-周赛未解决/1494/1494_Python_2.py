import collections
from typing import List


class Node:
    def __init__(self, i):
        self.i = i
        self.before = []
        self.next = []


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        # 生成有向无环图
        course_list = [Node(i) for i in range(1, n + 1)]
        basic_courses = {i for i in range(1, n + 1)}  # 当前可以入门学习的课程
        for dependency in dependencies:
            course_list[dependency[1] - 1].before.append(course_list[dependency[0] - 1])
            course_list[dependency[0] - 1].next.append(course_list[dependency[1] - 1])
            if dependency[1] in basic_courses:
                basic_courses.remove(dependency[1])

        # 拆分每个连通部分
        visited_course_1 = set()
        course_group_list = []
        for course in course_list:
            if course in visited_course_1:
                continue
            temp_visited = {course}
            now_course_list = collections.deque([course])
            while now_course_list:
                for i in range(len(now_course_list)):
                    now_course = now_course_list.popleft()
                    for next_course in now_course.before:
                        if next_course not in temp_visited:
                            now_course_list.append(next_course)
                            temp_visited.add(next_course)
                    for next_course in now_course.next:
                        if next_course not in temp_visited:
                            now_course_list.append(next_course)
                            temp_visited.add(next_course)
            visited_course_1 |= temp_visited
            course_group_list.append(temp_visited)

        # 计算每一门课程的前置深度
        course_group_depth = []
        for course_group in course_group_list:
            course_depth = {}
            for course in course_group:
                depth = 0
                now_course_list = collections.deque([course])
                while now_course_list:
                    depth += 1
                    for i in range(len(now_course_list)):
                        now_course = now_course_list.popleft()
                        for next_course in now_course.before:
                            now_course_list.append(next_course)
                course_depth[course.i] = depth

            # 获取前置深度列表
            depth_list = list(course_depth.values())

            # 计算前置深度数量
            depth_count = collections.Counter(depth_list)
            depth_num_list = [depth_count[i] for i in range(1, max(depth_list) + 1)]
            course_group_depth.append(depth_num_list)

        print(course_group_depth)

        # 计算最终需要的步数
        min_term = [len(depth_num_list) for depth_num_list in course_group_depth]  # 当前最少学期数（最长课程前置深度）

        # print("当前最少学期数:", min_term)

        need_term = 0
        already_learned = 0
        while already_learned < n:
            course_group_depth.sort(key=lambda x: len(x), reverse=True)
            need_term += 1
            now = k
            for depth_num_list in course_group_depth:
                if not depth_num_list:
                    continue
                if depth_num_list[0] <= now:
                    val = depth_num_list.pop(0)
                    now -= val
                    already_learned += val
                else:
                    val = now
                    depth_num_list[0] -= val
                    already_learned += val
                    break

            # print(course_group_depth)

        return need_term


if __name__ == "__main__":
    # 3
    print(Solution().minNumberOfSemesters(n=4, dependencies=[[2, 1], [3, 1], [1, 4]], k=2))

    # 4
    print(Solution().minNumberOfSemesters(n=5, dependencies=[[2, 1], [3, 1], [4, 1], [1, 5]], k=2))

    # 6
    print(Solution().minNumberOfSemesters(n=11, dependencies=[], k=2))

    # 5
    print(Solution().minNumberOfSemesters(
        n=5,
        dependencies=[[1, 5], [1, 3], [1, 2], [4, 2], [4, 5], [2, 5], [1, 4], [4, 3], [3, 5], [3, 2]], k=3))

    # 4
    print(Solution().minNumberOfSemesters(n=4, dependencies=[[1, 2], [4, 2]], k=1))

    # 6
    print(Solution().minNumberOfSemesters(n=12,
                                          dependencies=[[1, 2], [1, 3], [7, 5], [7, 6], [4, 8], [8, 9], [9, 10],
                                                        [10, 11], [11, 12]],
                                          k=2))

    # 4
    print(Solution().minNumberOfSemesters(n=12,
                                          dependencies=[[1, 2], [2, 3], [4, 5], [5, 6], [7, 8], [8, 9], [10, 11],
                                                        [11, 12]],
                                          k=3))
