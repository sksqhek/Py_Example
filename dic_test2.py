import re
import string

frequency = {}
document_text = open('text3.txt', 'rt')
line_count = 1;

while True:
    text_string = document_text.readline().lower()#한줄씩 읽기
    if text_string == '':#못읽어오면 파일 읽기종료
        break
    mach_pattern=re.findall(r'\b[a-z]{1,15}\b', text_string)

    for word in mach_pattern:
        list = frequency.get(word,0)
        if list == 0:#처음 저장이면
            frequency[word] = [line_count]#라인 추가
        else:
            frequency[word].append(line_count)#라인 추가

    line_count += 1#라인 증가

#단어를 기준으로 정렬
frequency_list = sorted(frequency.items(), key=lambda x: x[0])

print('words\t\t\tline numbers')
print('----------------------------')
for words in frequency_list:
    print(end="%-20s"%(words[0]))
    for i in range(len(frequency[words[0]])):#라인 위치는 리스트로 저장했기 때문에 리스트 길이 만큼 출력
        print(end="%d"%frequency[words[0]][i]);
        if i < len(frequency[words[0]]) - 1:#마지막에는 콤마 출력 않하게
            print(end=", ")
    print()