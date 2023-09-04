import subprocess

#78962
def delete_snort() :
    sid = input('Enter snort rule sid : ')

    local_rules_file_path = '/etc/snort/rules/local.rules'

    

    # subprocess.run(['vi', local_rules_file_path, 'echo', '/78', '\n', 'dd'])
    # # subprocess.run(['/' + sid, '\n'])
    # # subprocess.run(["0"])
    # # subprocess.run(["dd"])
    # # subprocess.run(["-c", ":wq"])

test = delete_snort()