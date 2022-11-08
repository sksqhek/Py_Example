class Node:
    prevNode = None  # 앞쪽 노드를 가리키는 변수
    data = None  # 데이터를 저장할 변수
    nextNode = None  # 뒤쪽 노드를 가리키는 변수

    def __init__(self, prevNode, data, nextNode):
        self.prevNode = prevNode
        self.data = data
        self.nextNode = nextNode


class DoublyLinkedList:
    nodeNum = None  # 노드의 수를 저장할 변수
    headNode = None  # 머리 노드를 가리키는 변수
    tailNode = None  # 꼬리 노드를 가리키는 변수

    #def __init__(self):#생성자는 1개만 가능
    #    self.nodeNum = 0

    # 연결 리스트 안의 노드 수 반환
    # len(DoublyLinkedList의 인스턴스)와 같이 사용
    def __len__(self):
        return self.nodeNum

    def AddFirst(self, data):
        oldHeadNode = self.headNode  # 기존의 머리 노드를 백업
        # 새로운 노드 생성
        # 이 노드가 새로운 머리 노드가 됨
        # 이 노드 앞에는 아무 노드도 연결되지 않음
        # 이 노드 뒤에 기존의 머리 노드가 연결됨
        newNode = Node(None, data, oldHeadNode)
        self.headNode = newNode  # 새로운 노드가 머리 노드가 됨
        # 기존에 연결 리스트가 비어 있었다면
        if oldHeadNode == None:
            # 꼬리 노드도 새로운 노드를 가리킴
            self.tailNode = newNode
        # 기존에 연결 리스트가 비어있지 않았다면
        else:
            # 기존의 머리 노드 앞에 새로운 노드를 연결
            oldHeadNode.prevNode = newNode
        self.nodeNum += 1

    def Addlast(self, data):
        newNode = Node(data, None)

        if self.headNode == None:
            self.headNode = newNode
        else:
            oldHeadNode = self.headNode

            while oldHeadNode != None:
                oldHeadNode = oldHeadNode.nextNode
        self.nodeNum += 1

    def Print(self):
        out = '[ '
        ptr = self.headNode  # 머리 노드에서부터 시작
        # 끝까지 반복하며 출력
        while ptr != None:
            out += str(ptr.data) + ' '
            # 다음 노드로 이동
            ptr = ptr.nextNode
        out += ']'
        print(out)

    def RemoveFirst(self):
        # 연결 리스트가 비어 있지 않으면
        if self.headNode != None:
            # 마지막 노드를 삭제하는 거라면
            if self.headNode.nextNode == None:
                # 연결 리스트를 비움
                self.headNode = None
                self.tailNode = None
            # 마지막 노드가 아니라면
            else:
                # 머리 노드의 다음 노드가 새로운 머리 노드가 됨
                self.headNode = self.headNode.nextNode
                # 이 노드 앞에는 아무 노드도 연결되지 않음
                self.headNode.prevNode = None
            self.nodeNum -= 1  # 노드 수 감소

    def RemoveLast(self):
        if self.headNode != None:
            if self.headNode.nextNode == None:
                self.headNode = self.headNode.nextNode
            else:
                prev = None
                ptr = self.headNode

                while ptr.nextNode != None:
                    prev = ptr
                    ptr = ptr.nextNode
                prev.nextNode = None
            self.nodeNum -= 1

    def __init__(self, maxsize):
        self.nodeNum = 0
        self.maxsize = maxsize
        self.top = 0
        self.items = [-1] * self.maxsize

    def Push(self, inputItem):
        self.items[self.top] = inputItem
        self.top += 1

    def Pop(self):
        self.items[self.top] = self
        self.top -= 1


DoublyLinkedList = DoublyLinkedList(10)
DoublyLinkedList.Push(1)

DoublyLinkedList.AddFirst(1)
DoublyLinkedList.Print()
DoublyLinkedList.AddFirst(2)
DoublyLinkedList.Print()
DoublyLinkedList.RemoveFirst()
DoublyLinkedList.Print()
DoublyLinkedList.Addlast(3)
DoublyLinkedList.Print()
DoublyLinkedList.Addlast(4)
DoublyLinkedList.Print()
DoublyLinkedList.RemoveLast()
DoublyLinkedList.Print()