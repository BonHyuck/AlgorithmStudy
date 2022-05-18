def solution(record):
    answer = []

    user_dict = {}
    command_arr = []

    for text in record:
        temp_arr = text.split()
        if temp_arr[0] != "Change":
            command_arr.append([temp_arr[0], temp_arr[1]])
        if temp_arr[0] != "Leave":
            user_dict[temp_arr[1]] = temp_arr[2]

    for com, user in command_arr:
        t = ""
        if com == "Enter":
            t = "님이 들어왔습니다."
        elif com == "Leave":
            t = "님이 나갔습니다."

        answer.append(user_dict[user] + t)

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))