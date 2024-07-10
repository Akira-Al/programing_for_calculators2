"""
data_ans.txtを複数のファイルから作成する
/data/data_ans_setの中で実行してください
"""

def load_raw_ans_data(file_path = "data_ans0.txt"):
  with open(file_path, 'r', encoding="utf-8") as f:
    all_lines = f.read()
    all_lines_list = all_lines.strip().split("\n")
    ans_list = [ [0,""] for _ in range(len(all_lines_list))]
    for i in range(len(all_lines_list)):
        line_list = all_lines_list[i].split(" ")
        if line_list[0] == "p":
            ans_list[i][0] = 1
        elif line_list[0] == "n":
            ans_list[i][0] = -1
        ans_list[i][1] = line_list[1]
    return ans_list

def load_raw_ans_data_list(file_path_list):
    ans_list = load_raw_ans_data(file_path_list[0])
    for file_path in file_path_list[1:]:
        for i in range(len(ans_list)):
            ans_list[i][0] += load_raw_ans_data(file_path)[i][0]

    for i in range(len(ans_list)):
        if ans_list[i][0] > 0.33*3:
            ans_list[i][0] = 1
        elif ans_list[i][0] < -0.33*3:
            ans_list[i][0] = -1
    return ans_list

def create_raw_ans_data(ans_list):
    file_path = "../data_ans.txt"
    with open(file_path, 'w', encoding="utf-8") as f:
        for ans in ans_list:
            if ans[0] == 1:
                f.write("p " + ans[1] + "\n")
            elif ans[0] == -1:
                f.write("n " + ans[1] + "\n")
            else:
                f.write("e " + ans[1] + "\n")
        

file_path_list = ["data_ans0.txt", "data_ans1.txt", "data_ans2.txt"]
ans_list = load_raw_ans_data_list(file_path_list)
create_raw_ans_data(ans_list)
