import subprocess

def delete_snort(path) :
    sid = input('Enter snort rule sid : ')

    # subprocess의 popen 함수를 사용해, vi 편집기를 실행
    # stdin, stdout, stderr 함수는 함수를 호출할 때 사용되는 인자이다.
    # 프로세스의 표준 입력, 표준 출력, 표준 오류를 어떻게 다룰지를 지정.
    process = subprocess.Popen(['vi', path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # vi가 열리면 문자열 검색 및 삭제 명령어 실행
    commands = [
        f'/sid:{sid};\n',             # 검색 명령어
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