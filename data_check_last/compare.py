import subprocess

failed_l = []
with open("res_pol_24_07_04[18:14:15].txt") as f:
    failed_l = f.readlines()
for i in range(len(failed_l)):
    failed_l[i] = failed_l[i].replace("\n", "")
prev_failed_l_look_up = []
num = 0
those_exist = []
for i in failed_l:
    res = subprocess.run(
        ["grep", i, "failed_txt_24_06_26[19:03:55].txt"],
        capture_output=True,
        text=True,
    ).stdout

    prev_failed_l_look_up += res

    if len(res) != 0:
        num += 1
        those_exist += [i]
