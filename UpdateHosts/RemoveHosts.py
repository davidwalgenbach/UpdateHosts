lines = []
with open (r"C:\Windows\System32\drivers\etc\hosts", 'r') as fp:
    lines = fp.readlines()
with open (r"C:\Windows\System32\drivers\etc\hosts", 'w') as fp:
    for line in lines:
        if "192.168.1.55" not in line:
            fp.write(line)