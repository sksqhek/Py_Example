import re

friends = {"홍길동": ["010-1234-5678", "친구", "한양대 정보통신과", "2019100164"], \
           "임꺽정": ["010-1111-2222", "가족", "-", "-"]}

def n():  # 줄 바꿈
    print()


def ShoutDown():  # 프로그램 종료
    print("<명함관리 프로그램>을 종료합니다.")
    exit()


def menu():  # main nenu
    print("\n  ++명함관리 프로그램++")
    print(")~~~~~~~~~~~~~~~~~~~~~~~~(")
    print(") 1. 명함 전체 출력      (")
    print(")~~~~~~~~~~~~~~~~~~~~~~~~(")
    print(") 2. 명함 추가           (")
    print(")~~~~~~~~~~~~~~~~~~~~~~~~(")
    print(") 3. 명함 삭제           (")
    print(")~~~~~~~~~~~~~~~~~~~~~~~~(")
    print(") 4. 명함 수정           (")
    print(")~~~~~~~~~~~~~~~~~~~~~~~~(")
    print(") 5. 명함 검색           (")
    print(")~~~~~~~~~~~~~~~~~~~~~~~~(")
    print(") 6. 명함 파일 불러오기  (")
    print(")~~~~~~~~~~~~~~~~~~~~~~~~(")
    print(") 7. 명함 파일 저장하기  (")
    print(")~~~~~~~~~~~~~~~~~~~~~~~~(")
    print(") 9. 종료                (")
    print(")~~~~~~~~~~~~~~~~~~~~~~~~(\n")


def name_list():  # 명함 목록
    print("----------------------------명함 목록---------------------------------\n")
    print(" <이름>", "%10s" % "<전화번호>", "%12s" % "<관계>", "%13s" % "<소속>", "%15s" % "<학번>")
    for name in friends:
        print("- {}".format(name) if len(name) == 3 else "- {}  ".format(name), "%15s" % "{}".format(friends[name][0]),
              "%9s" % "{}".format(friends[name][1]),
              "%10s" % "{}".format(friends[name][2]) if friends[name][1] == '-' else "%14s" % "{}".format(
                  friends[name][2]),
              "%16s" % "{}".format(friends[name][3]) if friends[name][2] == '-'
              else "%13s" % "{}".format(friends[name][3]))  # 전체 명함 목록 출
    print("------------------------------------------------------------------------")
    print("Total: {}\n".format(len(friends.keys())))  # Total: n

def add_list():
    print("<2. 명함 추가>\n")
    n()
    print("* 추가할 내용이 없으면 '-' 입력")
    print("* ex) 홍길동 010-1234-5678 가족 - -\n")
    print("<이름> <전화번호> <관계> <소속> <학번> 순으로 입력하세요 (띄어쓰기로 구분)\n")
    add_name, add_phone, add_relation, add_group, add_ID = input(":").split()  # 추가할 명함 입력
    n()

    for key in friends:
        if add_name == key:
            print("-'{}'명함은 이미 사용 중입니다. 다른 이름을 추가하여 주세요.\n".format(add_name))
            break
        if add_phone == friends[key][0]:
            print("-'{}'전화번호는 이미 사용 중입니다. 다른 번호을 추가하여 주세요.\n".format(add_phone))
            break

def del_list():
    while True:
        for key in friends:
            n()
            print("<3. 명함 삭제>\n")
            name_list()
            del_name, del_phone = input("삭제할 '이름'과 '전화번호'를 입력하세요 (띄어쓰기로 구분): ").split()
            if del_name not in friends:
                n()
                print("해당 명함은 존재하지 않습니다. 다시 확인하여 주십시오.\n")
            if del_phone not in friends[key]:
                n()
                print("해당 번호는 존재하지 않습니다. 다시 확인하여 주십시오.\n")

            if del_name in friends and del_phone in friends[key]:
                n()
                del (friends[del_name])
                print("-'{} : {}'님이 명함에서 삭제되었습니다.\n".format(del_name, del_phone))

        print("1. 계속 삭제\n" + "2. 메뉴로 돌아가기\n" + "3. 종료")
        print("-------------------------")
        selec2 = int(input("메뉴를 선택하세요: "))

        if selec2 == 2:
            break
        elif selec2 == 3:
            ShoutDown()

def edit_list():
    while True:
        n()
        print("<4. 명함 수정>\n")
        print("1. 이름 수정\n" + "2. 번호 수정\n" + "3. 관계 수정\n" + "4. 소속 수정\n" + "5. 학번 수정\n" + "6. 메뉴로 돌아가기\n")
        print("-------------------------")
        selec2 = int(input("메뉴를 선택하세요: "))
        n()

        # 1. 이름 수정
        if selec2 == 1:
            print("1. '이름 수정'을 선택하였습니다.\n")
            name_list()
            before_name = input("수정 전 이름(이름만 입력):")
            n()
            if before_name in friends:
                after_name = input("수정 후 이름(이름만 입력):")
                n()
                if after_name in friends:
                    print("해당 이름은 이미 사용 중입니다. 다른 이름을 사용하여 주십시오.\n")
                else:
                    print("-------------------------")
                    print("수정 되었습니다.\n")
                    print("-수정 전 '{} '".format(before_name))
                    friends[after_name] = friends[before_name]
                    friends.pop(before_name)
                    print("-수정 후 '{} '\n".format(after_name))
            else:
                n()
                print("해당 이름은 존재하지 않습니다. 다시 확인하여 주십시오.\n")
        elif selec2 == 2:
            print("2.'번호 수정'을 선택하였습니다.\n")
            name_list()
            before_phone = input("수정 전 전화번호(번호만 입력):")
            after_phone = ""
            n()

            isError = False
            for value in friends.values():
                if before_phone in value:
                    after_phone = input("수정 후 전화번호(번호만 입력):")
                    n()
                    break

            if after_phone == "":
                n()
                print("해당 번호는 존재하지 않습니다. 다시 확인하여 주십시오.\n")
                isError = True
            else:
                for value in friends.values():
                    if after_phone in value:
                        print("해당 번호는 이미 사용 중입니다. 다른 번호를 사용하여 주십시오.\n")
                        isError = True

            if isError == False:
                print("-------------------------")
                print("수정 되었습니다.\n")
                print("-수정 전 '{}'".format(before_phone))
                print("-수정 후 '{}'\n".format(after_phone))
                for key in friends:
                    if friends[key][0] == before_phone:
                        friends[key][0] = after_phone
                        break

        elif selec2 == 3:
            print("3. '관계 수정'을 선택하였습니다.\n")
            name_list()
            old_name = input("수정하고 싶은 이름을 입력하세요:")
            n()
            if old_name in friends:
                new_relation = input("수정할 관계를 입력하세요:")
                n()
                if new_relation in (friends[old_name][1]):
                    print("해당 관계는 이미 적용 중입니다.\n")
                # 수정 가능할 경우
                else:
                    print("-------------------------")
                    print("수정 되었습니다.\n")
                    print("-수정 전 '{} : {}'".format(old_name, friends[old_name][1]))
                    friends[old_name][1] = new_relation
                    print("-수정 후 '{} : {}'\n".format(old_name, new_relation))
        elif selec2 == 4:
            print("4. '소속 수정'을 선택하였습니다.\n")
            name_list()
            old_name = input("수정하고 싶은 이름을 입력하세요:")
            n()
            if old_name in friends:
                new_group = input("수정할 소속를 입력하세요:")
                n()
                if new_group in (friends[old_name][2]):
                    print("해당 소속는 이미 적용 중입니다.\n")
                # 수정 가능할 경우
                else:
                    print("-------------------------")
                    print("수정 되었습니다.\n")
                    print("-수정 전 '{} : {}'".format(old_name, friends[old_name][2]))
                    friends[old_name][2] = new_group
                    print("-수정 후 '{} : {}'\n".format(old_name, new_group))
        elif selec2 == 5:
            print("5. '학번 수정'을 선택하였습니다.\n")
            name_list()
            old_name = input("수정하고 싶은 이름을 입력하세요:")
            n()
            if old_name in friends:
                new_ID = input("수정할 학번을 입력하세요:")
                n()
                if new_ID in (friends[old_name][3]):
                    print("해당 학번은 이미 적용 중입니다.\n")
                # 수정 가능할 경우
                else:
                    print("-------------------------")
                    print("수정 되었습니다.\n")
                    print("-수정 전 '{} : {}'".format(old_name, friends[old_name][3]))
                    friends[old_name][3] = new_ID
                    print("-수정 후 '{} : {}'\n".format(old_name, new_ID))
        elif selec2 == 6:
            break

        print("1. 계속 수정\n" + "2. 메뉴로 돌아가기\n" + "3. 종료")
        print("-------------------------")
        selec2 = int(input("메뉴를 선택하세요: "))
        n()
        if selec2 == 1:  # 1. 다시 입력 받기
            continue
        elif selec2 == 2:  # 2. 메뉴로 돌아가기
            break
        else:  # 3. 프로그램 종료
            ShoutDown()

def search_list():
    while True:
        n()
        print("<5. 명함 검색>\n")
        print("1. 이름 검색\n" + "2. 번호 검색\n" + "3. 관계 검색\n" + "4. 소속 검색\n" + "5. 학번 검색\n" + "6. 메뉴로 돌아가기\n")
        print("-------------------------")
        selec2 = int(input("메뉴를 선택하세요:"))
        n()

        # 1. 이름 검색
        if selec2 == 1:
            print("1. '이름 검색'을 선택하였습니다.\n")
            find = input("검색할 이름을 입력하세요:")
        elif selec2 == 2:
            print("2. '번호 검색'을 선택하였습니다.\n")
            find = input("검색할 번호을 입력하세요:")
        elif selec2 == 3:
            print("3. '관계 검색'을 선택하였습니다.\n")
            find = input("검색할 번호을 입력하세요:")
        elif selec2 == 4:
            print("4. '소속 검색'을 선택하였습니다.\n")
            find = input("검색할 이름을 입력하세요:")
        elif selec2 == 5:
            print("5. '학번 검색'을 선택하였습니다.\n")
            find = input("검색할 번호을 입력하세요:")
        elif selec2 == 6:
            return

        print("----------------------------명함 목록---------------------------------\n")
        print(" <이름>", "%10s" % "<전화번호>", "%12s" % "<관계>", "%13s" % "<소속>", "%15s" % "<학번>")
        for key in friends:
            if selec2 == 1 and key == find or \
                    selec2 == 2 and friends[key][0] == find or \
                    selec2 == 3 and friends[key][1] == find or \
                    selec2 == 4 and friends[key][2] == find or \
                    selec2 == 5 and friends[key][3] == find:

                print("- {}".format(key) if len(key) == 3 else "- {}  ".format(key),
                      "%15s" % "{}".format(friends[key][0]),
                      "%9s" % "{}".format(friends[key][1]),
                      "%10s" % "{}".format(friends[key][2]) if friends[key][
                                                                          1] == '-' else "%14s" % "{}".format(
                          friends[key][2]),
                      "%16s" % "{}".format(friends[key][3]) if friends[key][2] == '-'
                      else "%13s" % "{}".format(friends[key][3]))  # 전체 명함 목록 출

        print("------------------------------------------------------------------------")
        n()

        print("1. 계속 검색\n" + "2. 메뉴로 돌아가기\n" + "3. 종료")
        print("-------------------------")
        selec2 = int(input("메뉴를 선택하세요: "))
        n()
        if selec2 == 1:  # 1. 다시 입력 받기
            continue
        elif selec2 == 2:  # 2. 메뉴로 돌아가기
            break
        else:  # 3. 프로그램 종료
            ShoutDown()


while True:
    menu()
    select1 = int(input("메뉴를 선택하세오: "))

    n()

    # 1. 명함 목록
    if select1 == 1:
        number = 1
        n()
        print("<1. 명함 목록>")
        n()
        name_list()

        print("1. 메뉴로 돌아가기\n" + "2. 종료\n")

        selec2 = int(input("메뉴를 선택하세요: "))
        n()
        if selec2 == 1:  # 1. 메뉴로 돌아기기
            continue
        elif selec2 == 2:  # 2. 프로그램 종료
            exit()


    # 2. 명함 추가
    elif select1 == 2:
        add_list()

    # 3. 명함 삭제
    elif select1 == 3:
        del_list()

    # 4. 명함 수정
    elif select1 == 4:
        edit_list()

    # 5. 명함 검색
    elif select1 == 5:
        search_list()

    # 6. 명함파일 불러오기
    elif select1 == 6:
        print("6. <명함 파일 불러오기>\n")
        try:
            friends = {}
            with open("ID_Card.txt", "r") as ID:
                ID.readline()
                ID.readline()
                ID.readline()
                for text in ID.readlines():
                    if len(text) == 1:
                        break

                    tok = [t.strip() for t in re.split('[ ]', text) if t]
                    if len(tok) == 5:
                        friends[tok[0]] = [tok[1], tok[2], tok[3], tok[4]]
                    elif len(tok) == 6:
                        friends[tok[0]] = [tok[1], tok[2], tok[3] + " " + tok[4], tok[5]]

            print("파일 불러오기 성공!!\n")

        except Exception as e:

            print("파일 불러오기를 실패하였습니다." + str(e))
            print("파일 경로를 확인하여 주십시오.\n")

        print("1. 메뉴로 돌아가기\n" + "2. 종료")
        print("-------------------------")
        selec2 = int(input("메뉴를 선택하시요:"))
        if selec2 == 1:  # 1. 메뉴로 돌아가기
            continue
        else:  # 3. 프로그램 종료
            ShoutDown()

    # 7. 명함 저장하기
    elif select1 == 7:
        print("7. <명함 파일 저장하기>\n")
        try:
            with open("ID_Card.txt", "w") as f:
                print("-----------------------<명함 리스트>------------------------------------\n", file=f)
                print("<이름>", "%12s" % "<전화번호>", "%12s" % "<관계>", "%13s" % "<소속>", "%13s" % "<학번>", file=f)
                for name in friends:
                    print("{}".format(name) if len(name) == 3 else "{}  ".format(name),
                          "%15s" % "{}".format(friends[name][0]),
                          "%9s" % "{}".format(friends[name][1]),
                          "%10s" % "{}".format(friends[name][2]) if friends[name][1] == '-' else "%14s" % "{}".format(
                              friends[name][2]),
                          "%16s" % "{}".format(friends[name][3]) if friends[name][2] == '-'
                          else "%13s" % "{}".format(friends[name][3]), file=f)
                print("", file=f)
                print("-------------------------------------------------------------------------", file=f)
            print("파일 저장 성공!!.\n")
            print("1. 저장 된 파일 확인하기\n" + "2. 메뉴로 돌아가기\n" + "2. 종료")
            print("-------------------------")
            selec2 = int(input("메뉴를 선택하시요:"))
            if selec2 == 1:
                try:
                    with open("ID_Card.txt", "r") as f:
                        for text in f:
                            print(text.strip())
                except:
                    print("파일 불러오기를 실패하였습니다.")
                    print("파일 경로를 확인하여 주십시오.\n")

            elif selec2 == 2:  # 2. 메뉴로 돌아가기
                continue
            else:  # 3. 프로그램 종료
                ShoutDown()

        except:
            print("파일 저장에 실패하였습니다.")
            print("파일 경로를 확인하여 주십시오.\n")

        print("1. 메뉴로 돌아가기\n" + "2. 종료")
        print("-------------------------")
        selec2 = int(input("메뉴를 선택하시요:"))
        if selec2 == 1:  # 1. 메뉴로 돌아가기
            continue
        else:  # 3. 프로그램 종료
            ShoutDown()

            # 9. 프로그램 종료
    elif select1 == 9:
        ShoutDown()
    else:
        print("잘못 입력하였습니다. 메뉴를 다시 선택하여 주십시오")




