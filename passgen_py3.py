#passgen 0.4.2#
import sys, random, string, subprocess, time
from random import choice
from os import urandom

print('''
.---..---..---..---..---..---..-..-.
| |-'| | | \ \  \ \ | |'_| |- | .` |
`-'  `-^-'`---'`---'`-'-/`---'`-'`-'
               0.4''')

def KeyGenerate():
	while True:
		try:
			result = ''.join(random.sample(char_set*6, int(bit_len)))
			print(result)
		except (KeyboardInterrupt):
			exit()

def NonConsecutive():
    NCKey = []
    while True:
        try:
            char_set = string.ascii_lowercase + string.ascii_uppercase
            index = int(bit_len)
            result = ''.join(random.sample(char_set*6, int(1)))
            if len(NCKey) < index:
                NCKey.append(str(result))
            print(''.join(NCKey))
            time.sleep(0.01)
            continue
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
            print(nextline)
            exit()
    except KeyboardInterrupt:
        proc.terminate()
        proc.wait()
        return
        exit()
    except Exception as e:
        print(e)
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
                char_set = string.ascii_lowercase
                bit_len = sys.argv[2]
                KeyGenerate()
            elif arg == '-b32':
                char_set = 'abcdefghijklmnopqrstuvwxyz234567'
                bit_len = sys.argv[2]
                KeyGenerate()
            elif arg == '-h':
                char_set = string.hexdigits
                bit_len = sys.argv[2]
                KeyGenerate()
            elif arg == '-lU':
                char_set = string.ascii_letters
                bit_len = sys.argv[2]
                KeyGenerate()
            elif arg == '-l1':
                bit_len = sys.argv[2]
                char_set = string.ascii_lowercase + string.digits
                KeyGenerate()
            elif arg == '-U1':
                char_set = string.ascii_uppercase + string.digits
                bit_len = sys.argv[2]
                KeyGenerate()
            elif arg == '-lU1':
                char_set = string.ascii_letters + string.digits
                bit_len = sys.argv[2]
                KeyGenerate()
            elif arg == '-U':
                char_set = string.ascii_uppercase
                bit_len = sys.argv[2]
                KeyGenerate()
            elif arg == '-NC':
                bit_len = sys.argv[2]
                NonConsecutive()
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
                        print(result)
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
