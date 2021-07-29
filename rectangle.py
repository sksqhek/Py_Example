# 빈리스트 만들고 숫자 10개 집어넣기
list1 = []
print("원하는 숫자를 10개 입력하세요.")
for i in range(1, 11):
    print(i, "번째 숫자:")
    num = int(input())
    list1.append(num)

print("원하는 숫자 10개를 추가하였습니다.")
print(list1)

# 정렬 후 찾아주길 원하는 숫자 입력받기
print("정렬을 하겠습니다.")
list1.sort()
print(list1)

print("10개의 숫자중 컴퓨터가 찾아주길 원하는 숫자를 하나 입력하세요")
n = int(input())

# 몇번째만에 맞추었는지 세어야 하니까 count 사용
count = 1

# 이진탐색을 위해
min = 0
max = len(list1) - 1
#seq = int((min + max) / 2)

while (min <= max):#범위 검사
    seq = int((min + max) / 2)#중간값 갱신
    if (list1[seq] == n):#() 가 아니라 [] 사용
        print("이 숫자가 맞나요?", list1[seq])#검사한 숫자 출력
        print("맞습니다.")
        print(count, "번 만에 맞추었습니다.")
        break
    elif (list1[seq] > n):
        print("이 숫자가 맞나요?", list1[seq])
        print("아닙니다. 더 작은 숫자입니다.")
        max = seq - 1
        count = count + 1
    else:
        print("이 숫자가 맞나요?", list1[seq])
        print("아닙니다. 더 큰 숫자입니다.")
        min = seq + 1
        count = count + 1