import re

def Function(fname, oper, num):
    fp = open(fname,"r")
    data = fp.read()

    if oper == "word":
        word = []
        for p in re.split("[ .,\n]", data):#단어 추출
            if p != '':
                word.append(p)

        word = set(word)#중복 단어 제거
        word = list(word)
        word.sort()#정렬

        for i in range(num):#입력한 수 만큼의 상위 단어 출력
            print(word[i])

    elif oper == "sen":
        sentence = data.split(".")

        for i in range(num):
            print(sentence[i].strip())

Function("our_vacation.txt", "word", 10)
Function("our_vacation.txt", "sen", 3)