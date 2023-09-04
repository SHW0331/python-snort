import subprocess

# 파일 경로 및 파일 이름을 지정합니다.
file_path = '/etc/snort/rules/local.rules'
search_string = '78'

# vi 명령어를 생성합니다.
vi_commands = f"""
/{search_string}
dd
:wq
"""

# vi를 호출하여 파일을 열고 명령어를 전달합니다.
try:
    result = subprocess.run(['vi', file_path], input=vi_commands.encode(), text=True, check=True)
    print(f'{search_string} 문자열이 삭제되었습니다.')
except subprocess.CalledProcessError as e:
    print('작업 실패.', e)
