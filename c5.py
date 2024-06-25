class ManagerInt:
    def __init__(self):
        self.subarrays = []

    def sumK(self, m, n):
        result = []
        path = []
        self.solve(m, 0, n, path, result)
        for subarray in reversed(result):
            print(", ".join(map(str, subarray)))

    def solve(self, m, index, target, path, result):
        if target == 0:
            result.append(path[:])
            return
        if index >= len(m) or target < 0:
            return
        self.solve(m, index + 1, target, path, result)
        path.append(m[index])
        self.solve(m, index + 1, target - m[index], path, result)
        path.pop()


k = ManagerInt()
m = [1, 4, 6, 3, 2, 2, 8]
n = 10
k.sumK(m, n)
