import subprocess

# snort create rules
# action, protocol, srcip~port, direction, dstip~port, options
def create_snort() :
    action = input("Enter action : ")
    protocol = input("Enter protocol : ")
    src_ip = input("Enter source ip : ")
    src_port = input("Enter source port : ")
    direction = input("Enter direction : ")
    dst_ip = input("Enter destination ip : ")
    dst_port =input("Enter destination port : ")
    
    options = []
    while True:
        
        option = input('Enter an option (msg:"option exmaple"; or "done" to finish) : ')

        if option.lower() == 'done':
            break 

        options.append(option)

    option_str = ' '.join(options)
    option = f"({option_str})"

    rule = f"{action} {protocol} {src_ip} {src_port} {direction} {dst_ip} {dst_port} {option}"
    return rule

#78962
def delete_snort() :
    sid = input('Enter snort rule sid : ')
    file_path = '/etc/snort/rules/local.rules'

    # subprocess의 popen 함수를 사용해, vi 편집기를 실행
    # stdin, stdout, stderr 함수는 함수를 호출할 때 사용되는 인자이다.
    # 프로세스의 표준 입력, 표준 출력, 표준 오류를 어떻게 다룰지를 지정.
    process = subprocess.Popen(['vi', file_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # vi가 열리면 문자열 검색 및 삭제 명령어 실행
    commands = [
        f'/{sid}\n',             # 검색 명령어
        'dd',                    # 현재 행 삭제 명령어
        ':wq\n',                 # 저장 및 종료 명령어
    ]

    # write 함수를 사용히여 vi 프로세스의 표준 입력으로 전송
    for command in commands:
        process.stdin.write(command.encode())
        process.stdin.flush()

    # vi 프로세스 대기 및 종료
    process.wait()

    # 결과 확인
    if process.returncode == 0:
        print(f'{sid} 문자열이 삭제되었습니다.')
    else:
        print('작업 실패.')


# snort restart
conf_file_path = '/etc/snort/rules/local.rules'
content = create_snort()

with open(conf_file_path, "a") as file:
    file.write(content)

print(f'added : {conf_file_path}')

command = ["snort", "-T", "-c", "/etc/snort/snort.conf"]
try:
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True, check=True)
    print(result)

except subprocess.CalledProcessError as e:
    print("Command failed with error:", e)
