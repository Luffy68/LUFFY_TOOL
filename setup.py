import subprocess
s = subprocess.getstatusoutput(f'pip3 install requests')
b = subprocess.getstatusoutput(f'pip3 install termcolor')
c = subprocess.getstatusoutput(f'pip3 install bs4')
r = subprocess.getstatusoutput(f'pip3 install re')

print(s[1])
print(" ")
print(b[1])
print(" ")
print(c[1])
print(" ")
print(r[1])