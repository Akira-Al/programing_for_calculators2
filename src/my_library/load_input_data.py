def load(file_path = "../data/train.txt"):
  with open(file_path, 'r', encoding="utf-8") as f:
    all_lines = f.read()
  all_lines_list = all_lines.strip().split("\n")
  res = []
  for all_lines in all_lines_list:
    res.append(all_lines.split("\t"))
  return res


def load_raw_data(file_path = "../data/data.txt"):
  with open(file_path, 'r', encoding="utf-8") as f:
    all_lines = f.read()
  all_lines_list = all_lines.strip().split("\n")
  return all_lines_list

def load_raw_ans_data(file_path = "../data/data_ans.txt"):
  with open(file_path, 'r', encoding="utf-8") as f:
    all_lines = f.read()
    all_lines_list = all_lines.strip().split("\n")
    ans_list = [ 0 for _ in range(len(all_lines_list))]
    for i in range(len(all_lines_list)):
        line_list = all_lines_list[i].split(" ")
        if line_list[0] == "p":
            ans_list[i] = 1
        elif line_list[0] == "n":
            ans_list[i] = -1
    return ans_list
