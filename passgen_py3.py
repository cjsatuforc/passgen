#passgen 0.4#
import sys, random, string, subprocess

print '''
.---..---..---..---..---..---..-..-.
| |-'| | | \ \  \ \ | |'_| |- | .` |
`-'  `-^-'`---'`---'`-'-/`---'`-'`-'
               0.4'''

def base32():
	while True:
		try:
			char_set = 'abcdefghijklmnopqrstuvwxyz234567'
			result = ''.join(random.sample(char_set*6, int(bit_len)))
			print result
		except (KeyboardInterrupt):
			exit()
def hexdigits():
	while True:
		try:
			char_set = string.hexdigits
			result = ''.join(random.sample(char_set*6, int(bit_len)))
			print result
		except (KeyboardInterrupt):
			exit()
def lowercase():
	while True:
		try:
			char_set = string.ascii_lowercase
			result = ''.join(random.sample(char_set*6, int(bit_len)))
			print result
		except (KeyboardInterrupt):
			exit()
def lowerupper():
	while True:
		try:
			char_set = string.ascii_lowercase + string.ascii_uppercase
			result = ''.join(random.sample(char_set*6, int(bit_len)))
			print result
		except (KeyboardInterrupt):
			exit()
def lowernum():
	while True:
		try:
			char_set = string.ascii_lowercase + string.digits
			result = ''.join(random.sample(char_set*6, int(bit_len)))
			print result
		except (KeyboardInterrupt):
			exit()
def uppernum():
	while True:
		try:
			char_set = string.ascii_uppercase + string.digits
			result = ''.join(random.sample(char_set*6, int(bit_len)))
			print result
		except (KeyboardInterrupt):
			exit()
def loweruppernum():
	while True:
		try:
			char_set = string.ascii_uppercase + string.ascii_lowercase + string.digits
			result = ''.join(random.sample(char_set*6, int(bit_len)))
			print result
		except (KeyboardInterrupt):
			exit()
def uppercase():
	while True:
		try:
			char_set = string.ascii_uppercase
			result = ''.join(random.sample(char_set*6, int(bit_len)))
			print result
		except (KeyboardInterrupt):
			exit()
def aircrack():
    arglist()
    characterset = raw_input('Enter permutation set: ')
    bit_len = raw_input('Enter character size: ')
    bssid = raw_input('Enter bssid: ')
    capfile = raw_input('Enter capfile: ')
    try:
        cmd = (['python passgen.py ' + characterset + ' | sudo aircrack-ng --bssid ' + bssid + ' -w- ' + capfile])
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        while proc.poll() == None:
            pcrackOut = proc.stdout
            nextline = proc.stdout.readlines()
            print nextline
            exit()
    except KeyboardInterrupt:
        proc.terminate()
        proc.wait()
        return
        exit()
    except Exception as e:
        print e
        proc.terminate()
        proc.wait()
        exit()
def arglist():
	print ('''options:\n -b32 [num] base32\n -h [num] hexdigits\n -l [num] lowercase\n -lU [num] lower and uppercase\n -l1 [num] lower and numerals\n -U [num] upper ascii\n -U1 [num] upper and numerals\n -lU1 [num] lower upper, and numerals\n -C [char] [num] custom character set and length\n -a aircrack-ng\n --help this list\n''')

args = sys.argv[1:]
try:
    if args:
        for arg in args:
            if arg == '-l':
                bit_len = sys.argv[2]
                lowercase()
            elif arg == '-b32':
                bit_len = sys.argv[2]
                base32()
            elif arg == '-h':
                bit_len = sys.argv[2]
                hexdigits()
            elif arg == '-lU':
                bit_len = sys.argv[2]
                lowerupper()
            elif arg == '-l1':
                bit_len = sys.argv[2]
                lowernum()
            elif arg == '-U1':
                bit_len = sys.argv[2]
                uppernum()
            elif arg == '-lU1':
                bit_len = sys.argv[2]
                loweruppernum()
            elif arg == '-U':
                bit_len = sys.argv[2]
                uppercase()
            elif arg == '--help':
                arglist()
            elif arg == '-a':
                aircrack()
            elif arg == '-C':
                while True:
                    try:
                        char_set = sys.argv[2]
                        char_len = sys.argv[3]
                        result = ''.join([random.choice(char_set) for _ in range(int(char_len))])
                        print result
                    except (IndexError):
                        print(IndexError, "Make sure you've added your character map and length")
                        exit()
                    except (ValueError):
                        print(ValueError, 'ValueError: sample larger than population')
                        exit()
                    except (KeyboardInterrupt):
                        exit()
    else:
        arglist()
except IndexError:
    arglist()
