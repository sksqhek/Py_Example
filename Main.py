import Theater

t = Theater.Theater(5, 9)

#좌석 예약
name = input("예약자 성함 : ")
rowChar = ord(input("열 입력 : "))
col = int(input("행 입력 : "))
numSeat = int(input("좌석 수 입력 : "))


print(t.reserve(name, rowChar, col, numSeat) and "성공" or "실패")

print(t.reserve("김신의", ord('A'), 5, 2) and "성공" or "실패")
print()

print(t.reserve("이윤수", ord('C'), 1, 3) and "성공" or "실패")
print()

print(t.reserve("강영훈", ord('D'), 4, 7) and "성공" or "실패")
print()

print(t.reserve("문종모", ord('C'), 7, 3) and "성공" or "실패")
print()
#좌석 취소
print(t.cancel(ord('A'), 6, 3))
print()

print(t.cancel2("이윤수"))
print()

#결과 출력
print()
t.printSeatMatrix()
t.getNumberOfReservedSeat()