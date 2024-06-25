class CheckArray:
    def __init__(self):
        self.ar1 = []
        self.ar2 = []
        
    def solve(self, ar1, ar2):
        m = len(ar1)
        n = len(ar2)
        k = m + n
        a = []
        i = 0
        j = 0
        cnt = 0
        while cnt <= k // 2 + 1:
            if i < m and (j >= n or ar1[i] <= ar2[j]):
                a.append(ar1[i])
                i += 1
            else:
                a.append(ar2[j])
                j += 1
            cnt += 1

        if k % 2 == 1:
            print(a[k // 2])
        print(a[k // 2 - 1])


ar1 = [1, 2, 5, 7, 8]
ar2 = [3, 4, 6]
k = CheckArray()
k.solve(ar1, ar2)

