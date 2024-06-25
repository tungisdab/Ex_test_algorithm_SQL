class DrawAnyShape:
    def __init__(self, n):
        self.n = n

    def draw(self):
        for i in range(1, self.n+1):
            print(" ", end="")
        print("*")
        for i in range(1, self.n):
            for j in range(1, self.n + 1 - i):
                print(" ", end = "")
            print("*", end="")
            for j in range(1, 2 * i):
                print(" ", end="")
            print("*", end="")
            print()
        print("*", end="")
        for i in range(1, self.n * 2):
            print(" ", end="")
        print("*")
        for i in range(1, self.n):
            for j in range(1, i+1):
                print(" ", end="")
            print("*", end="")
            for j in range(2 * self.n - 2 * i - 1):
                print(" ", end = "")
            print("*", end="")
            print()
        for i in range(1, self.n+1):
            print(" ", end="")
        print("*")

if __name__ == "__main__":
    n = int(input("Enter value for n: "))
    draw = DrawAnyShape(n)
    draw.draw()