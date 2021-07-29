M_INT = 9999
M_PATH = 6
path_name = 'ABCDEF'
path = []
for i in range(M_PATH):
    sub = [M_INT, M_INT, M_INT, M_INT, M_INT, M_INT]
    path.append(sub)

file = open("graph_input.txt", "rt")
file.readline()
for line in file:
    nums = line.split()
    path[path_name.find(nums[0])][path_name.find(nums[1])] = int(nums[2])

def dijkstra(start, end):
    di = [ M_INT, M_INT, M_INT, M_INT, M_INT, M_INT]
    chk = [ 0, 0, 0, 0, 0, 0]
    pre = [ 0, 0, 0, 0, 0, 0]

    idx = 0
    #최단거리 탐색
    di[start] = 0
    for i in range(M_PATH):
        min = M_INT
        for j in range(M_PATH):
            if chk[j] == 0 and di[j] < min:
                idx = j
                min = di[j]

        chk[idx] = 1
        if min == M_INT:
            return

        for j in range(M_PATH):
            if di[j] > di[idx] + path[idx][j]:
                di[j] = di[idx] + path[idx][j]
                pre[j] = idx;

        if idx == end:
            break

    save_data = []
    #탐색 경로 출력
    print(path_name[start], path_name[end], sep="\t\t", end="\t\t");

    save_data.append(path_name[start]);
    save_data.append(path_name[end]);

    pre_idx = 0
    top = 0
    pre_path = [ 0, 0, 0, 0, 0, 0];
    for i in range(M_PATH):
        pre_idx = i
        top = 0
        if pre_idx != start:
            if chk[i] > 0 and pre_idx == end:
                while(True):
                    pre_path[top] = pre_idx;
                    top += 1
                    pre_idx = pre[pre_idx];
                    if pre_idx == start:
                        break


                pre_path[top] = pre_idx

                tmp = ""
                while top >= 0:
                    print(path_name[pre_path[top]], end="");
                    tmp += path_name[pre_path[top]]
                    top -= 1

                    if top >= 0:
                        print(",",end="")
                        tmp += ","
    save_data.append(tmp)

    print("%20d"%di[end]);
    save_data.append(di[end])

    return save_data


save_file = open("2017.txt", "wt")
for i in range(1, M_PATH):
    save_data = dijkstra(0, i)
    save_file.write("%-10s %-10s %-10s %10s\n"%(save_data[0], save_data[1], save_data[2], save_data[3]))
