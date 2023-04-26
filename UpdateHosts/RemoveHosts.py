from queue import Empty


lines = []
with open (r"C:\Windows\System32\drivers\etc\hosts", 'r') as fp:
    lines = fp.readlines()
with open (r"C:\Windows\System32\drivers\etc\hosts", 'w') as fp:
    for line in lines:
        if "plasmatraxdb_tester" not in line and line != Empty:
            fp.write(line)