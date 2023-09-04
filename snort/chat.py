import subprocess

# 파일 경로 및 파일 이름을 지정합니다.
file_path = '/etc/snort/rules/local.rules'
search_string = '78'

# vi를 호출하여 파일 열기
process = subprocess.Popen(['vi', file_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# vi가 열리면 문자열 검색 및 삭제 명령어 실행
commands = [
    f'/{search_string}\n',   # 검색 명령어
    'dd',                   # 현재 행 삭제 명령어
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
    print(f'{search_string} 문자열이 삭제되었습니다.')
else:
    print('작업 실패.')
