# Editing Objects #

## format ##
each object is 9 bytes. 
The struct is as follows

TT   = object type
XXXX = horizontal position
YYYY = vertical position
ZZ   = per-object flags
SS   = object parameters
VV   = tiles to read from the VRAM
WW   = tiles to read from the VRAM when the object is reversed
 -- repeat until
FF   = end of object list (only appears once)

## Properties for All objects ##
$28 $00 $02 $90 $03 -- set at 7078C
## Selecting Object Types ##
|Type code | What it is |
| :--- | :--- |
| 01 | ?????? |
| 02 | ?????? |
| 03 | ?????? |
| 04 | ?????? |
| 05 | ?????? |
| 06 | ?????? |
| 07 | ?????? |
| 08 | ?????? |
| 09 | ?????? |
| 0A | ?????? |
| 0B | ?????? |
| 0C | ?????? |
| 0D | ?????? |
| 0E | ?????? |
| 0F | Smoke Plume |
| 10 | Blinky Block |
| 11 | ?????? |
| 12 | Some Boss |
| 13 | ?????? |
| 14 | ?????? |
| 15 | Game crashes |
| 16 | ?????? |
| 17 | Starts as brick, turns into some sled |
| 18 | End of level sign |
| 19 | dragonfly guy shows up and sonic just runs solo |
| 20 | Some ground only enemy |
| 21 | Some ground only enemy |
| 22 | ?????? |
| 23 | Pogo enemy |
| 24 | mine enemy |
| 25 | Some ground only enemy | 
| 26 | ?????? |
| 27 | some oscillating enemy that moves up down (small) |
| 28 | floating up and down platform |
| 29 | some oscillating enemy that moves up down (big) |
| 2A | some oscillating enemy that moves up down (big) |
| 2B | some oscillating enemy that moves up down (big) |
| 2C | some oscillating enemy that moves up down (medium) |
| 2D | some animation that disappears |
| 2E | some animation that disappears |
| 2F | Spring boot thing from SEZ |

## Setting position ##
It seems like we adjust everything from TOPLEFT of the map.
This explains the simple pattern:
Left | Top are decreasing values
Right | Down are increasing values

- Bytes 2-3 (Nibbles 3-6) control the HORIZONTAL value
    - Byte 2 (Nibbles 3-4): micro adjustments
        - To Go Left: Lower number
        - To Go Right: Increase number
    - Byte 3 (Nibbles 5-6): macro adjustments
        - To Go Left: Lower number
        - To Go Right: Increase number
- Bytes 4-5 (Nibbles 7-10) control the VERTICAL value
    - Byte 4 (Nibbles 7-8): micro adjustments
        - to go UP: decrease value
        - to go DOWN: increase value
    - Byte 5 (Nibbles 9-10): macro adjustments
        - to go UP: decrease value
        - to go DOWN: increase value



## Editing Tiles to use ##
 - TODO