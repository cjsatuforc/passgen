Porting to Julia attempts to fix the speed issues found in python as of this writing The julia port out performs python by a huge margin
<br>
<br>
Julia - lowercase at 10 character length = 253,301K/s, CPU 27%
<br>
<br>
Python - lowercase at 10 character length = 92,135K/s, CPU 100%
<br>
<br>
As of 02/07/16 The julia port is a working replacement for Passgen.py and will continue to be developed ahead of the
python version.
<br>
<br>
Dependencies[Nettle]
<br>
Pkg.add("Nettle")
<br>
<br>
Command line arguments are as followed
<br>
<br>
lowercase = -l [num] -n
<br>
uppercase = -u [num] -n
<br>
lower + upper = -lu [num] -n
<br>
lower + upper + nums = -lun [num] -n
<br>
lower + num = -ln [num] -n
<br>
upper + num = -un [num] -n
<br>
<br>
The third argument can be replaced with -ntlm to generate windows hashes.
