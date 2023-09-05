import subprocess

# r : 읽기, w : 쓰기, a : 추가
def modify_snort() :

    # print(
    # "\n"
    # "Refer to the information below for what to modify. \n"
    # "alert --> (1) \n"
    # "protocol --> (2) \n"
    # "src ip --> (3) \n"
    # "src port --> (4) \n"
    # "direction --> (5) \n"
    # "dst ip --> (6) \n"
    # "dst port --> (7) \n"
    # "options --> (8) \n"
    # )

    sid = input("Enter sid : ")
    file_path = '/etc/snort/rules/local.rules'

    file_read = subprocess.run(["cat", f"{file_path}"], capture_output=True, text=True)
    lines = file_read.stdout.split('\n')

    result_list = []

    for line in lines:
        if f'sid:{sid}' in line:
            result_list = line
            break

    print(result_list)
    rule_parts = result_list.split()

test = modify_snort()
