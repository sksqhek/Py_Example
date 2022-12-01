heroes = [ "아이언맨", "캡틴아메리카", "블랙위도우", "닥터스트레인지" ]
print("1) 최초 리스트:", heroes)

print("2) 2번 인데스 값 추출:", heroes[2])

heroes[3] = "토르"
print("3) 3번 인데스 값을 토르로 변경:", heroes)


heroes.insert(4, "블랙팬서")
print("4) 4번 인데스에 블랙팬서 삽입:", heroes)

heroes.append("타노스")
print("5) 타노스 추가:", heroes)

heroes.remove("타노스")
print("6) 타노스 삭제:", heroes)

print("7) 전체 항목의 개수:", len(heroes))

sort_heroes = sorted(heroes)
print("8) 오름차순 정렬:", sort_heroes)

for h in heroes:
    print(h)


