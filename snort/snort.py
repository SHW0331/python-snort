import subprocess
import modify as md
import delete as dele
import create as crt

# snort restart
file_path = '/etc/snort/rules/local.rules'

select = input('Enter the snort action (create, delete, modify) : ')
print('\n')
if select == 'create' :
    content = crt.create_snort(file_path)
elif select == 'delete' :
    content = dele.delete_snort(file_path)
elif select == 'modify' :
    content = md.modify_snort(file_path)
else:
    print('Error')

command = ["snort", "-T", "-c", "/etc/snort/snort.conf"]
try:
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True, check=True)
    print(result)

except subprocess.CalledProcessError as e:
    print("Command failed with error:", e)
