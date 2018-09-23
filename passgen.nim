##Passgen for Nim 0.18.0
import os, strutils, hashes, random, parseopt

#Compiler options
{.deadCodeElim:on, checks:off, hints:off, warnings:off.}

var
  asciiGen = @["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  digitGen = @["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  hashGen = newSeq[string](0)


echo "Hash Length: "
let hashLen = readLine(stdin)

proc main =
  randomize()
  var v = 0
  for v in countup(0, parseInt(hashLen) - 1):
    shuffle(asciiGen)
    hashGen.add(asciiGen[v])
  let hashString = join(hashGen)
  echo hashString
main()

