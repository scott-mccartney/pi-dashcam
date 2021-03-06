import subprocess
import shlex

header = []

def parse_header(line):
    header = shlex.split(line)
        
def parse_mem(line):
    mem = shlex.split(line)
    size = mem[1]
    used = mem[2]
    avail = mem[3]
    
    return avail

def run_command(cmd):
    avail = 0
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)

    i = 0
    while True:
        output = proc.stdout.readline()
        if output == '' and proc.poll() is not None:
            break
        if output:
            if i==0:
                parse_header(output)
            if i==1:
                avail = parse_mem(output)
            i += 1
            
    rc = proc.poll()
    if rc==0:
        return avail
    else:
        return -1

command = 'df'
mem = run_command(shlex.split(command))
print mem
