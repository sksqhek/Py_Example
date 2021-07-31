import re
import string

frequency = {}
document_text = open('a_star.py', 'rt', encoding='UTF8')
text_string = document_text.read().lower()
mach_pattern=re.findall(r'\b[a-z]{3,15}\b', text_string)


for word in mach_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

#frequency_list = frequency.keys()
#빈도스로 정렬후(빈도스가 많은순으로) 결과를 튜플로 리턴
frequency_list = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

for words in frequency_list:
    print(words[0], frequency[words[0]])



