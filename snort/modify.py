import subprocess
import re

# r : 읽기, w : 쓰기, a : 추가
def modify_snort(path) :

    sid = input("Enter sid : ")
    with open(path, "r") as file:
        file_content = file.read()

    lines = file_content.split('\n')

    original_content = ''
    for line in lines:
        if f'sid:{sid}' in line:
            original_content = line
            break;

    print(f"\n{original_content} \n")
    print(
    "Refer to the information below for what to modify. \n"
    "alert --> 1 \n"
    "protocol --> 2 \n"
    "src ip --> 3 \n"
    "src port --> 4 \n"
    "direction --> 5 \n"
    "dst ip --> 6 \n"
    "dst port --> 7 \n"
    "options --> 8 \n"
    )
    select = input("Enter the category you want to modify : ")

    if(select == '8'):
        1
    else:
        modify = input("Enter the contents : ")

    # [6]= dst_port 까지 저장.
    rule_parts = original_content.split()

    if select == '1':
        rule_parts[0] = f'{modify}'
        modify_rule = " ".join(rule_parts)
    elif select == '2':
        rule_parts[1] = f'{modify}'
        modify_rule = " ".join(rule_parts)
    elif select == '3':
        rule_parts[2] = f'{modify}'
        modify_rule = " ".join(rule_parts)
    elif select == '4':
        rule_parts[3] = f'{modify}'
        modify_rule = " ".join(rule_parts)
    elif select == '5':
        rule_parts[4] = f'{modify}'
        modify_rule = " ".join(rule_parts)
    elif select == '6':
        rule_parts[5] = f'{modify}'
        modify_rule = " ".join(rule_parts)
    elif select == '7':
        rule_parts[6] = f'{modify}'
        modify_rule = " ".join(rule_parts)
    elif select == '8':
        # for i in range (len(options_name)):
        #     if(options_name[i] == modify):
        # 정규화로 option을 항목 별로 구분
        # 괄호 제거
        pattern = r'\((.*?)\)'
        match = re.search(pattern, original_content)
        options = match.group(1)
        print(f'\noriginal rules = {options}')
        print('Existing rules will be deleted.\n')

        options_modify = []
        while True:
            option = input('Enter an option contents (msg:"option exmaple"; or "done" to finish) : ')    
            if option.lower() == 'done':
                break   
            options_modify.append(option)  
        option_str = ' '.join(options_modify)
        option = f"({option_str})"

        modify_rule = f"{rule_parts[0]} {rule_parts[1]} {rule_parts[2]} {rule_parts[3]} {rule_parts[4]} {rule_parts[5]} {rule_parts[6]} {option}"
        
        # 이 부분은 아직 수정 중
        # # options을 항목 별로 나누기 위해 ; 기준으로 나눔
        # options_result = options.split(';')
        # length = len(options_result)
        # print(options_result) # ['msg:"Test modify.py"', ' sid:123456', ' test:123', '']

        # option을 : 기준으로 다시 나눠주고 항목의 이름을 변수에 저장
        # options_name = []
        # for i in range(length - 1):
        #     options_parts = options_result[i].split(':')
        #     options_name.append(options_parts[0].replace(" ", ""))
        #     print(options_parts[1]) # "Test modify.py"

        #     if(options_name[i] == options_item):
        #         options_parts[1] = f'{options_content}'
        #         options_modify = ":".join(options_result)
        #         print(options_modify)

        # for i in range(len(options_name)):
        #     if(options_item == options_name[i])

    else:
        select = -1
        print("Entered it incorrectly.")
    

    if(select == -1):
        print("Please select an option between 1 and 8.")
    else:
        print('\nThe rule has been modified.')
        print(modify_rule)

        # 기존 rule 삭제 후, modify_rule 추가
        process = subprocess.Popen(['vi', path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # vi가 열리면 문자열 검색 및 삭제 명령어 실행
        commands = [
            f'/sid:{sid};\n',             # 검색 명령어
            'dd',                    # 현재 행 삭제 명령어
            ':wq\n',                 # 저장 및 종료 명령어
        ]

        for command in commands:
            process.stdin.write(command.encode())
            process.stdin.flush()
        process.wait()

        with open(path, "a") as file:
            file.write(modify_rule)