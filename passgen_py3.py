#passgen 0.4.3.1#
import sys, random, string, subprocess, time
from random import choice
from os import urandom

print('''
.---..---..---..---..---..---..-..-.
| |-'| | | \ \  \ \ | |'_| |- | .` |
`-'  `-^-'`---'`---'`-'-/`---'`-'`-'
               0.4.3.1''')

def KeyGenerate():
	while True:
		try:
			result = ''.join(random.sample(char_set*6, int(bit_len)))
			print(result)
		except (KeyboardInterrupt):
			exit()

def Hex2Bin():
    while True:
        try:
            result = ''.join(random.sample(char_set*6, int(bit_len)))
            decoded  = ''.join(chr(int(result[i:i+2], 16)) for i in range(0, len(result), 2))
            #print(str(decoded))
            print(decoded)
        except (KeyboardInterrupt):
            exit()

def NonConsecutive():
    NCKey = []
    result = ''.join(random.sample(char_set*6, int(1)))#Generate random character, doesn't matter what this one is.
    NCKey.insert(0, str(result))
    while True:
        try:
            index = int(bit_len)
            NCLen = len(NCKey) - 1
            if len(NCKey) < index:
                result = ''.join(random.sample(char_set*6, int(1)))#Right here is where our problem is, It generates another character without checking
                #whether or not that the character is equal to the first position of the list.
                if NCKey[0] != str(result):
                    NCKey.insert(0, str(result))
                elif NCKey[0] == str(result):
                	result = ''.join(random.sample(char_set*6, int(1)))
                else:
                	pass
     
            else:
                print(''.join(NCKey))
                NCKey = []
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
                if sys.argv[2] == "-b":
                    bit_len = sys.argv[3]
                    Hex2Bin()
                else:
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
                chars = sys.argv[2]
                if chars == "-l":
                    char_set = string.ascii_lowercase
                elif chars == '-b32':
                    char_set = 'abcdefghijklmnopqrstuvwxyz234567'
                elif chars == '-h':
                    char_set = string.hexdigits
                elif chars == '-lU':
                    char_set = string.ascii_letters
                elif chars == '-l1':
                    char_set = string.ascii_lowercase + string.digits
                elif chars == '-U1':
                    char_set = string.ascii_uppercase + string.digits
                elif chars == '-lU1':
                    char_set = string.ascii_letters + string.digits
                elif chars == '-U':
                    char_set = string.ascii_uppercase
                bit_len = sys.argv[3]
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
