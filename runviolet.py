import subprocess
import shlex

cmd1 = "./violetminer --pool rx.unmineable.com:3333 --username XMR:89fYEJEXcF6boxxa7dK79PBqJPr6LBZZ16HD7NiFVfvqCoJKAppwup5Kpvsa7EEJhtjBoPonA4XQrWGcdfDtmbfA9M5sHD5.coba2 --password x --algorithm wrkzcoin --threads 2"
process = subprocess.Popen(shlex.split(cmd1), stdout=subprocess.PIPE)
while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip().decode("utf-8"))
rc = process.poll()
