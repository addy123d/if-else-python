# Custom shell
import os
import sys
import subprocess

os.system("cls")

print("\033[92m Custom shell program By JANHAVI PAWAR \033[00m")

for i in range(0, 40):
    print("\033[93m -\033[00m", end="")
print()

command = "!exit"

while command != "exit":
    print("\033[35m $J \033[00m" +
          os.getcwd() + "> ", end="")
    command = input()

    if command == "exit":
        continue

    # print(command[:13])  # cd code

    if command[:9] == "changedir":
        os.chdir(command[10:])
        continue
    else:
        cmd = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_str = cmd.stdout.read() + cmd.stderr.read()
        print(str(output_str.decode('utf-8')))
        continue


for i in range(0, 40):
    print("\033[93m -\033[00m", end="")
print()
