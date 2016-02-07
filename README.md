#Passgen for Julia 0.1.9
Please refer to the julia.md file as well as passgen.jl for information on this code.
<br>
The julia port is superior to the python version in terms of speed and size

# Passgen for Python 0.4.5
Passgen is an alternative for the random character generator crunch which attempts to solve cracking WPA/WPA2 keys by randomizing the output opposed to generating a list like so, (aaaaaaaa, aaaaaaab, aaaaaac, etc)..

example usuage with aircrack-ng (python passgen.py -l | sudo aircrack-ng --bssid 00:11:22:33:44:55 -w- WiFi.cap)

argument switches are as followed
<br>
-b32 [num] base32
<br>
-h [num] hexcode
<br>
-l [num] lowercase ascii
<br>
-l1 [num] lowercase ascii + digits(0-9)
<br>
-U [num] uppercase ascii
<br>
-U1 [num] uppercase ascii + digits
<br>
-lU [num] lowercase + uppercase ascii
<br>
-lU1 [num] lowercase + uppercase ascii + digits
<br>
-C [char] [length] custom character set + length
<br>
-a aircrack-ng
<br>
-NC (-NC -lU1 8) Nonconsecutive with permutations character set and character length
<br>
-ntlm [char] [length] Windows Hash bruteforce attack

This application will be updated with new features as needed.

#Changelog
v0.4.5
<br>
Added -ntlm switch
<br>
v0.4.4
<br>
Fixed -NC switch, Nonconsecutive character set works properly now.
<br>
v0.4.3.4
<br>
Added SpeedTest switch
<br>
[WIP] added -NC switch for nonconsecutive character permutation sets, Still giving issues but the code logic has been worked out.
<br>
v0.4
<br>
Added new character length commandline argument
<br>
v0.3.7:Added -a for aircrack-ng support
<br>
Added in version 0.3.2
<br>
base32 and hexdigits(merged fork)
<br>
Made the options listing more pretty.

#Planned features for 0.4.6
<br>
New algorithm that mimics hashcats Mask attack.
<br>
Cleaning up redundant character permutation code
<br>
getting -NC to work with -a, -ntlm, -C
<br>
Adding new character permutations
<br>
Multithread support(Attempting to speed up key generation)

#Screenshot
![alt tag](http://i.imgur.com/cXWBSpm.png)
