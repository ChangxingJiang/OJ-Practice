def read4(buf4):
    return 0


class Solution:
    def read(self, buf, n):
        now, remain = 0, n
        while True:
            cache = [" "] * 4
            size = read4(cache)
            for i in range(min(remain, size)):
                buf[now] = cache[i]
                now += 1
            remain -= size
            if size < 4 or remain <= 0:
                return now


if __name__ == "__main__":
    pass
