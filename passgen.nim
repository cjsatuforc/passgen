##Passgen for Nim 0.18.0
import os, strutils, hashes, random, parseopt

#Compiler options
{.deadCodeElim:on, checks:off, hints:off, warnings:off, optimization:speed.}
var
  asciiGen = @["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  digitGen = @["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
proc main =
  proc genHash(asciiPick: string lengthPick: int): string {.discardable.} =
    randomize()
    of cmdLongOption:
      case key
      of "u", "l", "d", "ul", "ud", "ld", "uld":

      case value
      of lengthPick
