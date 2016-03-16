Porting to Julia attempts to fix the speed issues found in python as of this writing The julia port out performs python by at least 95%.(Processor speed dependent of course)
<br>
<br>
Julia - lowercase at 10 character length = 968,085K/s(Intel core i3 2.5Ghz dual core + dual hyperthread), CPU 27%
<br>
<br>
Python - lowercase at 10 character length = 92,135K/s(Intel core i3 2.5Ghz dual core + dual hyperthread), CPU 100%
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
The third argument allows different forms of output(-n(normal), -ntlm(md4_Windows hash), -p(Permutations)
