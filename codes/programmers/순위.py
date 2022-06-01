def solution(n, results):
    answer = 0

    arr = [[0 for _ in range(n)] for _ in range(n)]
    for winner, loser in results:
        winner -= 1
        loser -= 1
        arr[winner][loser] = 1
        arr[loser][winner] = -1

    for cur_player in range(n):
        this_player_win = []
        for other_player in range(n):
            if arr[cur_player][other_player] == 1:
                this_player_win.append(other_player)
        while this_player_win:
            loser = this_player_win.pop()
            for compare_player in range(n):
                if arr[loser][compare_player] == 1 and arr[cur_player][compare_player] == 0:
                    arr[cur_player][compare_player] = 1
                    arr[compare_player][cur_player] = -1
                    this_player_win.append(compare_player)

    for player in arr:
        if player.count(0) == 1:
            answer += 1


    return answer





print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))