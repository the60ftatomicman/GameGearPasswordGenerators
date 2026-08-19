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
## Selecting Object Types (Based on what I see Existing in Roms) ##
|Type code | What it is | Object Flags | Object params | Applicable Zones |
| :--- | :--- | :--- | :--- | :--- |
| 09 | - | 00 | 00 = ??<br> 01 = ?? | THZ<br>GPZ<br>MGHZ<br>APZ<br>EEZ |
| 0C | - | 00 | 00 | APZ |
| 10 | TV Monitors | 00 | 08 = Tails 1up<br>06 = star invincibility<br>05 = stopwatch<br>04 = rocket shoes<br>03 = speed shoes<br>02 = sonic 1up<br>01 = rings | THZ<br>GPZ<br>SEZ<br>MGHZ<br>APZ<br>EEZ |
| 17 | - | 00 | 02 | EEZ |
| 18 | - | 00 | 00 | THZ<br>GPZ<br>SEZ<br>MGHZ<br>APZ<br>EEZ |
| 1B | - | 00 | 00 | THZ<br>GPZ<br>SEZ<br>MGHZ |
| 20 | - | 00 | 00 =<br>01 = | SEZ |
| 21 | - | 00 =<br>10 = | 16 =<br>0A =<br>08 =<br>06 =<br>03 =<br>04 =<br>02 =<br>01 = | THZ<br>MGHZ |
| 23 | - | 00 | 00 =<br>01 = | SEZ |
| 24 | - | 00 | 00 | MGHZ |
| 25 | - | 00 | 0B =<br>0A =<br>09 =<br>08 =<br>07 =<br>04 = | GPZ |
| 26 | - | 00 | 92 =<br>8C =<br>8A =<br>88 =<br>87 =<br>86 =<br>01 =<br>00 = | THZ<br>GPZ<br>SEZ<br>EEZ |
| 27 | - | 10 | 00 | THZ |
| 28 | - | 00 | 8B =<br>89 =<br>86 =<br>84 =<br>83 =<br>0A =<br>05 =<br>04 = | THZ<br>GPZ<br>SEZ<br>MGHZ<br>EEZ |
| 2C | - | 00 | 00 =<br> 01 =<br>| GPZ<br>EEZ |
| 2E | - | 00 | 00 | MGHZ |
| 2F | Riding Spring | 00 | 00 | SEZ<br>MGHZ |
| 30 | - | 00 | 00 | APZ |
| 36 | - | 00 | 12 =<br>0E =<br>0C =<br>0A =<br> | EEZ |
| 38 | - | 00 | 00 =<br> 01 =<br> | EEZ |
| 3C | - | 00 | 00 =<br> 01 =<br> | APZ |
| 3D | - | 00 | 08 =<br> 04 =<br>08 = | APZ |
| 3F | - | 00 | 8B =<br> 86 =<br>83 = | APZ |
| 50 | THZ Boss   | 00 | 00 | THZ  |
| 51 | GPZ Boss   | 00 | 00 | GPZ  |
| 54 | SEZ Boss   | 00 | 00 | SEZ  |
| 56 | MGHZ Boss  | 00 | 00 | MGHZ |
| 59 | APZ Boss   | 00 | 00 | APZ  |
| 5E | EEZ Boss 1 | 00 | 00 | EEZ  |
| 60 | EEZ Boss 2 | 00 | 00 | EEZ |

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