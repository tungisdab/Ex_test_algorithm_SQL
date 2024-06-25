'''

x = int(input())
n = int(input())
print((1 - x ** (n + 1)) // (1 - x))

'''

class Solve:
    def __init__(self, x, n) :
        self.x = x
        self.n = n

    def answer(self):
        if self.x == 1:
            return self.n + 1 
        return (1 - self.x ** (self.n + 1)) // (1 - self.x)

if __name__ == "__main__":
    x = int(input("Nhập x: "))
    n = int(input("Nhập n: "))
    solver = Solve(x, n)
    result = solver.answer()
    print(result)