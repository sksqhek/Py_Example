import Seat

class Theater:
    seats = []
    rowCount = 0
    colCount = 0
    def __init__(self, rowCount, colCount):
        if rowCount > 26:
            rowCount = 26

        for i in range(rowCount):
            self.seats.append([])
            for j in range(colCount):
                self.seats[i].append(Seat.Seat())

        self.rowCount = rowCount
        self.colCount = colCount

    def getRowIndex(self, uppercaseChar):
        return uppercaseChar - ord('A')

    def reserve(self,name, rowChar, col, numSeat):
        print(name + "님 이름으로 " + chr(rowChar) + str(col) + "부터 " + str(numSeat) +"개의 좌석 예약: ")

        if self.getRowIndex(rowChar) > self.rowCount or col > self.colCount or numSeat + col - 1 > self.colCount:
            return False
        else:
            for i in range(col,col + numSeat):
                c = self.seats[self.getRowIndex(rowChar)][col]
                if c.isOccupied():
                    return False

        for i in range(col-1,col+numSeat-1):
            s = self.seats[self.getRowIndex(rowChar)][i]
            s.reserve(name)

        self.printSeatMatrix();
        return True

    def cancel2(self, name:str):
        count = 0
        for i in range(self.rowCount):
            for j in range(self.colCount):
                s = self.seats[i][j]
                if s.isOccupied() and s.match(name):
                    s.cancel()
                    count += 1

        self.printSeatMatrix();
        return name + "님의 좌석 취소: 총 " + str(count) + "개의 좌석이 취소되었습니다."


    def cancel(self, rowChar:int, col:int, numSeat:int):
        count = 0
        for i in range(col-1, col+numSeat-1):
            s = self.seats[self.getRowIndex(rowChar)][i];
            if s.isOccupied():
                s.cancel()
                count += 1

        self.printSeatMatrix()
        return "" + chr(rowChar) + str(col) + "부터 좌석 " + str(numSeat) + "개 취소: 총 " + str(count) + "개의 좌석이 취소되었습니다."

    def getNumberOfReservedSeat(self):
        count = 0
        for i in range(self.rowCount):
            for j in range(self.colCount):
                s = self.seats[i][j]
                if s.isOccupied():
                    count += 1

        print("총 " + str(count) + "개의 좌석이 예약되었습니다.");

    def printSeatMatrix(self):
        print("   ", end='')
        for i in range(1, 10):
            print("   " + str(i), end='')
        print()


        for i in range(self.rowCount):
            print(chr(ord('A') + i) + ": ", end='')
            for j in range(self.colCount):
                s = self.seats[i][j]
                if s.isOccupied():
                    print("[X]", end='')
                else:
                    print("[0]", end='')
            print()
