def solution(places):

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def find_result(room):
        for r in range(5):
            for c in range(5):
                if room[r][c] == 'P':
                    queue = []
                    for k in range(4):
                        new_r = r + dr[k]
                        new_c = c + dc[k]
                        if 0 <= new_r < 5 and 0 <= new_c < 5:
                            if room[new_r][new_c] == 'P':
                                return 0
                            elif room[new_r][new_c] == 'O':
                                queue.append([new_r, new_c])
                    while queue:
                        rr, cc = queue.pop(0)
                        for k in range(4):
                            new_rr = rr + dr[k]
                            new_cc = cc + dc[k]
                            if 0 <= new_rr < 5 and 0 <= new_cc < 5 and (r != new_rr or c != new_cc):
                                if room[new_rr][new_cc] == 'P':
                                    return 0
        return 1



    answer = []
    for i in range(5):
        place = places[i]
        arr = []
        for p in place:
            arr.append(list(p))
        answer.append(find_result(arr))
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))