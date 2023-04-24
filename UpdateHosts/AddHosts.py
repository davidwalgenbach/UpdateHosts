lines = []
with open (r"C:\Windows\System32\drivers\etc\hosts", 'r') as fp:
    lines = fp.readlines()
lines.append("192.168.1.55\tplasmatraxdb_tester")
with open (r"C:\Windows\System32\drivers\etc\hosts", 'w') as fp:
    for line in lines:
        fp.write(line)