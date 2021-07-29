import random


class Person:
    def __init__(self, name, addr, tel):
        self.name = name
        self.addr = addr
        self.tel = tel


class Student(Person):
    def __init__(self, name, addr, tel, major):
        super().__init__(name,addr,tel)
        self.major = major
        self.subject = ["국어", "영어","수학"]
        self.score = []

#학생정보 리스트에 저장
list = [Student("Kim", "서울", "010 1111 1111", "전자"),
        Student("Leem", "수원", "010 2222 2222", "산공"),
        Student("Park", "용인", "010 3333 3333", "기계"),]

#점수 3개 추가
for s in list:
    s.score.append(random.randint(0,100))
    s.score.append(random.randint(0, 100))
    s.score.append(random.randint(0, 100))
    s.score.append((s.score[0] + s.score[0] + s.score[0])/3)#4번째에 평균 저장


def printStudentInfo():
    for s in list:
        print(s.name, s.addr, s.tel, s.major)


def printRank():
    list.sort(key=lambda x: x.score[3],reverse=True)
    i = 1
    for s in list:
        print("%d %-5s %.2f"%(i, s.name, s.score[3]))
        i += 1

printStudentInfo()

printRank()


