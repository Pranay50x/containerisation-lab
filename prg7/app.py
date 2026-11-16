import os, sys 

if len(sys.argv) != 2: 
    print("Use properly")

host = sys.argv[1] 
resp = os.system(f"ping -c 4 {host}")
if resp == 0: 
    print(f"{host} is reachable")
else:
    print(f"{host} is unreachable")
