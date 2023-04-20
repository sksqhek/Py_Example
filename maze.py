class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.top = 0
        self.items = [0,0] * self.maxsize

    def push(self, inputItem):
        if self.top == self.maxsize:
            print("Stack is full")
            return
        self.items[self.top] = inputItem
        self.top += 1

    def pop(self):
        if self.top == 0:
            print("Stack is empty")
            return None
        self.top -= 1
        return self.items[self.top]

    def print_stack(self):
        out = 'stack = ['
        for i in range(self.top):
            out += str(self.items[i])
            if i < self.top - 1:
                out += ', '
        out += ']'
        print(out)

    def is_empty(self):
        return self.top == 0

def Push_Loc(stack, x, y, maze, MAZE_SIZEX, MAZE_SIZEY):
    if x < 0 or y < 0 or x >= MAZE_SIZEX or y >= MAZE_SIZEY:
        return

    if maze[x][y] != 'X' and maze[x][y] != '.':
        stack.push([x,y])

if __name__ == '__main__':
    stack = Stack(maxsize=10)

    maze = []
    fp = open("maze.txt", "r")

    for f in fp:
        m = []
        f = f.strip()
        for i in f:
            m.append(i)
        maze.append(m)

    cur = [0,0]

    MAZE_SIZEX = len(maze[0])
    MAZE_SIZEY = len(maze)

    #start position search
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                cur = [i, j]

    print("startPosition : ")
    print((cur[1], cur[0]), "-> ")

    while maze[cur[0]][cur[1]] != 'G':
        x = cur[0]
        y = cur[1]

        maze[x][y] = '.' # 방문한 곳을 표시

        #이동 가능한 곳을 탐색
        Push_Loc( stack, x + 1, y, maze, MAZE_SIZEX, MAZE_SIZEY)
        Push_Loc( stack, x - 1, y, maze, MAZE_SIZEX, MAZE_SIZEY)
        Push_Loc( stack, x, y + 1, maze, MAZE_SIZEX, MAZE_SIZEY)
        Push_Loc( stack, x, y - 1, maze, MAZE_SIZEX, MAZE_SIZEY)

        if stack.is_empty():
            print("이동경로를 찾을 수 없습니다. 실패")
            exit(0)
        else:
            cur = stack.pop(); #현재 좌표를 변경
            print("(%d, %d) -> "%(cur[1], cur[0]))

    print("도착")
    print("탐색 성공")