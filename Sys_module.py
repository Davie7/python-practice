import sys
# sys stands for system.

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

print(sys.argv) # gives the path of the current directory.
