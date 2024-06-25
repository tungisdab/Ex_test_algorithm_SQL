class ArrIntManager:
    def __init__(self, arrInt=None):
        self.arrInt = arrInt if arrInt is not None else []
    
    def set_array(self, arrInt):
        self.arrInt = arrInt

    def get_array(self):
        return self.arrInt
    
    def solveA(self):
        return sum(self.arrInt)
    
    def solveB(self):
        return sum([i for i in self.arrInt if check(i)])
    
    def solveC(self):
        n = len(self.arrInt)
        for i in range(0, n - 2):
            if self.arrInt[i] + self.arrInt[i+1] == self.arrInt[i+2]:
                print(self.arrInt[i], self.arrInt[i+1], self.arrInt[i+2])
    
    def solveD(self):
        arrInt = self.arrInt
        n = len(arrInt)
        lis = [1 for _ in range(n)]
        lds = [1 for _ in range(n)]

        # Duyệt theo hướng tăng
        for i in range(1, n):
            for j in range(i):
                if arrInt[i] > arrInt[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1

        # Duyệt theo hướng giảm
        for i in reversed(range(n - 1)):
            for j in reversed(range(i - 1, n)):
                if arrInt[i] > arrInt[j] and lds[i] < lds[j] + 1:
                    lds[i] = lds[j] + 1

        # Tìm dãy con tăng giảm ổn định dài nhất
        maxLength = 0
        maxIndex = -1
        for i in range(n):
            totalLength = lis[i] + lds[i] - 1
            if totalLength > maxLength:
                maxLength = totalLength
                maxIndex = i

        result = []
        i = maxIndex
        while i >= 0 and arrInt[i] == arrInt[maxIndex]:
            result.append(arrInt[i])
            i -= 1

        i = maxIndex + 1
        while i < n and arrInt[i] < arrInt[maxIndex]:
            result.append(arrInt[i])
            i += 1

        return maxLength, result

def check(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    arrInt = [1, 2, 3, 5, 4, 1, 3, 4, 5, 4, 5, 9, 7, 0, 11, 13, 10, 23]
    manager = ArrIntManager(arrInt)  
    resultA = manager.solveA()  
    print(resultA)

    retultB = manager.solveB()
    print(retultB)

    resultC = manager.solveC()
    print(resultC)
    resultD = manager.solveD()
