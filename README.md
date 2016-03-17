#Passgen for Julia 0.2.2
The julia port is superior to the python version in terms of speed and size
<br>
<br>
Arguments: "julia passgen.jl -l 10 -n"
<br>
           "julia passgen.jl [character set] [length] [type]"
<br>


#Character set lists
-l lowercase
<br>
-u uppercase
<br>
-n numeral
<br>
Alternates for the switches are as followed and correspond to the list above
<br>
-lu, -ln, -un, -lun
<br>
-b32 creates a base32 generation
<br>
#Type switches
-norm normal generation
<br>
-perm permutation on each generation until competed and then follows to the next generation...etc
<br>
-ntlm generation md4 hashes based on the character generation
