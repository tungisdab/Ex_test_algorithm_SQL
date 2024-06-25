from collections import Counter
from difflib import SequenceMatcher

class MyString:
    def __init__(self, s):
        self.s = s
    
    def solveA(self):
        ans = 0 
        for i in self.s:
            ans += ord(i)
        return ans
    
    def solveB(self):
        ans = 0
        for i in self.s:
            x = i.upper()
            if i == x and i.isalpha():
                ans += ord(i)
        return ans
    
    def solveC(self):
        a = [i for i in self.s if i != " "]
        a = "".join(a)
        n = int(input("Nhập n: "))
        x = Counter(a)
        z = sorted(x.items(), key=lambda x: x[1])
        k = n 
        a = []
        for i in z:
            if i[1] >= n and i[0].isalpha(): 
                if i[1] > k and len(a) > 0:
                    b = ", ".join(a)
                    print(b + ": " + str(k)) 
                    a.clear()
                    k += 1
                a.append("\'" + i[0] + "\'")
        if len(a) > 0:
            b = ", ".join(a)
            print(b + ": " + str(k)) 
    
    def solveD(self):
        # string1 = "fffffapple pie available"
        # string2 = "come have some ffapple piesfafsdfasf"
        string1 = input("Nhập chuỗi 1: ")
        string2 = input("Nhập chuỗi 2: ")
        match = SequenceMatcher(None, string1, string2).find_longest_match()

        print(string1[match.a:match.a + match.size])  
        # print(string2[match.b:match.b + match.size])  

if __name__ == "__main__":
    s = "Hello programers. Im Developer"
    # s = "a"
    myString = MyString(s)
    resultA = myString.solveA()
    print(resultA)

    resultB = myString.solveB()
    print(resultB)
    
    myString.solveC()
    myString.solveD()
