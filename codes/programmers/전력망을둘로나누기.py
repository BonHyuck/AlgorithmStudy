def solution(n, wires):
    answer = float('inf')

    connection = [[0 for _ in range(n)] for _ in range(n)]
    # 연결 체크
    for i, j in wires:
        i -= 1
        j -= 1
        connection[i][j] = 1
        connection[j][i] = 1

    # 1개 끊기
    for i, j in wires:
        i -= 1
        j -= 1
        connection[i][j] = 0
        connection[j][i] = 0

        visited = [0 for _ in range(n)]
        visited[0] = 1
        queue = [0]
        while queue:
            point = queue.pop(0)
            for idx, check in enumerate(connection[point]):
                if check == 1 and visited[idx] == 0:
                    visited[idx] = 1
                    queue.append(idx)

        connection[i][j] = 1
        connection[j][i] = 1

        answer = min(answer, abs(visited.count(1) - visited.count(0)))

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))