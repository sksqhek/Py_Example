class MyMatrix:
    def getNewMatrix(self,n):
        if type(n) is not int:#정수가 아닌경우
            return -1
        if n < 3 or n % 2 == 0:#3보다 작거나 짝수라면
            return -1

        List = []

        for row in range(n):
            row_list = []
            for col in range(n):
                row_list.append(n)
            List.append(row_list)

        nn = n - 2
        for i in range(1, int(n / 2 + 1)):
            for r in range(i, nn + 1):
                for c in range(i, nn + 1):
                    List[r][c] *= n
            nn -= 1

        return List


matrix = MyMatrix()

param = int(input("정수 입력:"))

result = matrix.getNewMatrix(param)

if result == -1:
    print("입력 에러")
else:
    for m in result:
        for n in m:
            print("%5d"%(n),end="\t")
        print()
