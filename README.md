# Passgen 0.4
Passgen is an alternative for the random character generator crunch which attempts to solve cracking WPA/WPA2 keys by randomizing the output opposed to generating a list like so, (aaaaaaaa, aaaaaaab, aaaaaac, etc).


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

This application will be updated with new features as needed.

#Changelog
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

#Planned features for 0.4.3
Support for popular tools such as aircrack baked in.
<br>
Adding new character permutations
<br>
Multithread support(Attempting to speed up key generation)

#Screenshot
![alt tag](http://i.imgur.com/cXWBSpm.png)
