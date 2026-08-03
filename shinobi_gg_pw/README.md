# GG Shinobi 2 PW Generator

It's a great game, but boy is it HARD.
Here's a generator to get you to start with ANY possible state that is available to generate via the 


# Files

password_gg_shinobi.html - a simple HTML form with JS generating the output.

password_gg_shinobi.py - the same method but in a python script.

# The Password Algorithm
So you have *5* characters who can have a value *0-F*.
From LEFT to RIGHT we'll call them: *P0-P4*

example: if we had DF012; P0 == D, P4 == 2

So first some *TERMS* for the formula<br>
N = Desired number of Ninjas<br>
C = the Crystal Bitmap we want ot use<br>
H = the desired Health count we want (4, 6, 8, 10, 12 only)<br>
K = the encryption "key"

P0 = (N - (2 * K)) and 0xF<br>
P1 = C<br>
P2 = (H + K) and 0xF<br>
P3 = (N + C + H) and 0xF<br>
P4 = K

## Checksums
We need to ensure that:<br>

P4 / K != 0<br>

P3 == (<br>
     ((P2 - P4) & 0x0F)<br>
    + P1<br>
    + ((P0 + 2 * P4) & 0x0F)<br>
) & 0x0F<br>


## Other Oddities
So the game will sometimes provide you with different passwords like 1F6D7. which is the same as "full everything" DFD01. Why? Not certain! In testing it made no difference.

## How was this made
it is 2026 so you can imagine: it was an agentic (AI) effort with the stock ChatGPT  model and Claude for the html.
First I found which RAM addresses mapped to which game variables.
| RAM Address | What it impacts | Explaination |
| -------- | -------- | -------- |
| C024 | Current Life | If we had 5 health bars and 3 were present, this would would be 03. Not password tracked |
| C025 | Maximum Life | If we had 5 health bars and 3 were present, this would would be 05 |
| C027 | Crystals acquired | It's a 4-bit mask<br>(so only the lower nibble of this address is used)<br>Byte 0 = Yellow<br>Byte 1 = Green<br>Byte 2 = Blue<br>Byte 3 = Pink<br>The full map<br>01 = Yellow<br>02 = Green<br>03 = Yellow, Green<br>04 = Blue<br>05 = Yellow,Blue<br>06 = Green,Blue<br>07 = Yellow, Green,Blue<br>08 = Pink<br>09 = Yellow,Pink<br>0A = Green,Pink<br>0B = Yellow, Green,Pink<br>0C = Blue,Pink<br>0D = Yellow,Blue,Pink<br>0E = Green,Blue,Pink<br>0F = Yellow, Green,Blue,Pink<br>|
| C028 | Ninjas acquired | it's a 5-bit mask oddly enough,both nibbles are used.<br>LowerNibble<br>Byte 0 == unused<br>Byte 1 == Toggles BLUE<br>Byte 2 == Toggles YELLOW<br>Byte 3 == Toggles PINK<br>HigherNibble<br>Byte 4 == Toggles GREEN<br>Byte 6 == unused<br>Byte 7 == unused<br>Byte 8 == unused<br><br>Full Mapping Looks like this<br>00 -> 01 = RED<br>02 -> 03 = RED/BLUE<br>04 -> 05 = RED/YELLOW<br>06 -> 07 = RED/BLUE/YELLOW<br>08 -> 09 = RED/PINK<br>0A -> 0B = RED/BLUE/PINK<br>0C -> 0D = RED/YELLOW/PINK<br>0E -> 0F = RED/BLUE/YELLOW<br>10 -> 11 = RED/GREEN<br>12 -> 13 = RED/BLUE/GREEN<br>14 -> 15 = RED/YELLOW/GREEN<br>16 -> 17 = RED/BLUE/YELLOW/GREEN<br>18 -> 19 = RED/PINK/GREEN<br>1A -> 1B = RED/BLUE/PINK/GREEN<br>1C -> 1D = RED/YELLOW/PINK/GREEN<br>1E -> 1F = RED/BLUE/YELLOW/GREEN<br>|
| C040 | Players/Continues | how many continues we get. Not password tracked |
| C041 | Ninjitsu Magic | 0-9, how much magic we have. Not password tracked |
| C042->C045 | Score | these values + 00 for the tens and ones make your score. direct Hex to value representation. |

FROM this chart, I was able to debug in Emulicious when we wrote to these values when I input a proper password.
Passing those labels to chatGPT we found:
_LABEL_1341_ is where we figure out which sprites to display on the PW screen for the digits. it's a straight forward 1-1 affair.  
_DATA_2346A_ is the mapping for the digits to something but its absolutely visual not decypher logic.  
_LABEL_1363_ Looks like it's where do do the PW logic. When I set the READ BP on my range above, we jump to here and do stuff. Nice!
AI debugged the routine, I verified it against my known logic and voila! an algorithm was uncovered.
ChatGPT wrote the python script for me, Claude converted to a simple JS function and created a form for me.



# Bonus RAM addresses for GG Shinobi 1
You can't save a password here but you can enter a CHEAT
| RAM | Values | Explaination |
| --- | ------ | ------------ |
| D20B | 0-A | current health  |
| D20C | 0-A | max health      |
| D21C | 0-F | Ninja available (0f is all)|
| D21D | 0-9 |Players (+1 count, so 06 == 5) |
| D21E | 0-9 | Ninja Magic |
