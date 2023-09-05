import re

lines = [
    '# $Id: local.rules,v 1.11 2004/07/23 20:15:44 bmc Exp $',
    '# ----------------',
    '# LOCAL RULES',
    '# ----------------',
    '# This file intentionally does not come with signatures.  Put your local',
    '# additions here.',
    '',
    '',
    '',
    '',
    'alert tcp 192.168.0.187 any -> 192.168.209.128 any (msg:"Test modify.py"; sid:123456; test:123;)'
]


sid = input("Enter sid : ")

result_list = []
for line in lines:
    if f'sid:{sid}' in line:
        result_list = line
        break

# [6]= dst_port 까지 저장.
rule_parts = result_list.split()

# 정규화로 option을 항목 별로 구분
# 괄호 제거
pattern = r'\((.*?)\)'
match = re.search(pattern, result_list)
options = match.group(1)

# options을 항목 별로 나누기 위해 ; 기준으로 나눔
options_result = options.split(';')
length = len(options_result)

# option을 : 기준으로 다시 나눠주고 항목의 이름을 변수에 저장
options_name = []
for i in range(length - 1):
    options_parts = options_result[i].split(':')
    options_name.append(options_parts[0].replace(" ", ""))

print(options_name[0])
print(options_name[1])
print(options_name[2])