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
First, XY Coords to make things easier to test to validate or play with said objects.
These points will put an object next to Sonic at the start.
- THZ1 $00 $02 $90 $03  -- set at 705AE for first object to spawn near sonic
- GPZ1 $00 $02 $60 $02  -- set at 70959 for first object to spawn near sonic
- SEZ1 $10 $02 $CD $03  -- set at 70DF7 for first object to spawn near sonic
- MGHZ1 $10 $02 $CD $02 -- set at 710C1 for first object to spawn near sonic (for coconut do 70 01 for Y axis)
- APZ1 $10 $02 $CD $01  -- set at 713C1 for first object to spawn near sonic
- EEZ1 $20 $02 $6D $04  -- set at 71631 for first object to spawn near sonic

## Selecting Object Types (Based on what I see Existing in Roms) ##
|Type code | What it is | Applicable Zones | Object Flags | Object params | Sprite Settings Per Zone |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 09 | Single Ring | THZ<br>GPZ<br>MGHZ<br>APZ<br>EEZ | 00 | 00 = ??<br> 01 = ?? | THZ = 00,00<br>GPZ = 00,00<br>MGHZ = 00,00<br>APZ = 00,00<br>EEZ = 00,00 |
| 0C | Bubbles? | APZ | 00 | 00 | APZ = 8E,8E|
| 10 | TV Monitors | THZ<br>GPZ<br>SEZ<br>MGHZ<br>APZ<br>EEZ | 00 | 08 = Tails 1up<br>06 = star invincibility<br>05 = stopwatch<br>04 = rocket shoes<br>03 = speed shoes<br>02 = sonic 1up<br>01 = rings | THZ = 00,00<br>GPZ = 00,00<br>SEZ = 00,00<br>MGHZ = 00,00<br>APZ = 00,00<br>EEZ = 00,00 |
| 17 | Elevator | EEZ | 00 | 02 | EEZ = B2,B2|
| 18 | End Level Spinner | THZ<br>GPZ<br>SEZ<br>MGHZ<br>APZ<br>EEZ | 00 | 00 | THZ = 00,00<br>GPZ= 00,00<br>SEZ = 00,00<br>MGHZ = 00,00<br>APZ = 00,00<br>EEZ = 00,00 |
| 1B | Pop up Spikes | THZ<br>GPZ<br>SEZ<br>MGHZ | 00 | 00 | THZ = 00,00<br>GPZ = 00,00<br>SEZ = 00,00<br>MGHZ = 00,00 |
| 20 | Badnick, fireball/yam looking guy | 00 | 00 = ??<br> 01 = ?? | SEZ = A4,A4 |
| 21 | Badnick, lady bug spring guy | THZ<br>MGHZ | 00 = Moves Right first<br>10 = moves left first| 16 =<br>0A =<br>08 =<br>06 =<br>03 =<br>04 =<br>02 =<br>01 = | THZ = 86,98<br>MGHZ = 7C,8E |
| 23 | Badnick, pogostick guy | SEZ | 00 | 00 = ??<br> 01 = ?? | SEZ = 86,86 |
| 24 | Metal Coconut Bomb | MGHZ | 00 | 00 = Fall left<br> 01 = Fall Right | MGHZ = A0,A0 |
| 25 | Badnick, elephant with shooter | GPZ | 00 | 0B =<br>0A =<br>09 =<br>08 =<br>07 =<br>04 = | GPZ = 96,A8 |
| 26 | hidden spring | THZ<br>GPZ<br>SEZ<br>EEZ | 00 | 92 = yellow<br>8C =Invis<br>8A =Invis<br>88 =<br>87 =<br>86 =<br>01 = Yellow<br>00 = nothing| THZ = 72,72<br>GPZ = 72,72<br>SEZ = 72,72<br>EEZ = 9E,9E(or0) |
| 27 | Badnick, hornet drone | THZ | 10 | 00 | THZ = AA,AA |
| 28 | Floating Platform - No Drop | THZ<br>GPZ<br>SEZ<br>MGHZ<br>EEZ | 00 | 8B =<br>89 =<br>86 =<br>84 =<br>83 =<br>0A =<br>05 =<br>04 = | THZ = 6A,(0,13,19)<br>GPZ = 6A,(0B,0C,0E,18)<br>SEZ = 6A,(18,1C,30,6A)<br>MGHZ = 6A,(07,0A,0C,0F,10,12,14,19,1C,6A)<br>EEZ = 6A,(00,08,0B,10,11) |
| 2C | Badnick, hornet drone | GPZ<br>EEZ | 00 | 00 =<br> 01 =<br>| GPZ = 8C,8C<br>EEZ = 94,94 |
| 2E | Slowing Mud? Must be level with ground | MGHZ | 00 | 00 | MGHZ = 72,(13,1B) |
| 2F | Riding Spring | SEZ<br>MGHZ | 00 | 00 | SEZ = 94,94<br>MGHZ = AC,AC |
| 30 | red vertical spring up | APZ | 00 | 00 | APZ = 86,86 |
| 36 | Laser Turret Down | EEZ | 00 | 12 =<br>0E =<br>0C =<br>0A =<br> | EEZ = 76,76 |
| 38 | Badnick, bomb droid | EEZ | 00 | 00 =<br> 01 =<br> | EEZ = 72,72 |
| 3C | Spear Upwards | APZ | 00 | 00 =<br> 01 =<br> | APZ = 6A,6A |
| 3D | Badnick, Hot Dog guy | APZ | 00 | 08 =<br> 04 =<br>08 = | APZ = 70,70 |
| 3F | Brown platform | APZ | 00 | 8B =<br> 86 =<br>83 = | APZ = 80,(32,00) |
| 50 | THZ Boss   | THZ  | 00 | 00 | THZ  = 00,00 |
| 51 | GPZ Boss   | GPZ  | 00 | 00 | GPZ  = 00,00 |
| 54 | SEZ Boss   | SEZ  | 00 | 00 | SEZ  = 00,00 |
| 56 | MGHZ Boss  | MGHZ | 00 | 00 | MGHZ = 00,00 |
| 59 | APZ Boss   | APZ  | 00 | 00 | APZ  = 00,00 |
| 5E | EEZ Boss 1 | EEZ  | 00 | 00 | EEZ  = 00,00 |
| 60 | EEZ Boss 2 | EEZ  | 00 | 00 | EEZ  = 00,00 |

# Steps to manipulate objects #
Here is a simple guide as to how you can set an object ANYWHERE in ANY level

## Basic Understanding ##
Read the table above. Every "object" is really a series of 9 bytes.
Let's use an example

10,70,03,CE,02,00,06,00,00

This is a monitor, at location *figure this math out later* and it's a star invicibility monitor.
How do I know this? let's break it apart
1 byte = 2 of the digits (or a number between a comma in this example)

| Type | X coordinates (macro,micro) | Y coordinates (macro,micro) | flags | params | tiles (normal,reverse) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 10 | 70,03 | CE,02 | 00 | 06 | 00,00 |

- **Type** control the logic for the object you will put on screen as as well as how it draws it's tiles
- **X coordinates** A macro and a Micro number. Sets your X value for the object. see **Setting Position** for details
- **Y coordinates** A macro and a Micro number. Sets your X value for the object. see **Setting Position** for details
- **Flags** Usually just used to determine if an object will move right (forward) or left (reverse).
- **Params** Various other bits of logic are determined by this value
- **Tiles** which tiles (as matching to a direct index in the TILE view in the Emulicious editor) to use for the object

We will read these all in starting at the beginning of the object list until we hit the byte defined as **FF**

With this in mind here is the simple changes cheat sheet:
- To move things
    - update **XY Coordinates**, to change what something is, change the

- To change an object to something new
    - Pull up the **Selecting Object Types** in this guide 
    - Find the **type** to be what you match. write it down
    - Write down ALL the values you see in the **Selecting Object Types** for that type.
    - Ensure that type is usable in your zone via the **Applicable Zones** column
    - Find the memory location for the object you want to modify
        - this is easier said than done, will make this easier
    - change the **type** byte of the object in ROM to the value in the list.
    - change the **flags**,and **params** bytes if necessary
    - change the **tiles** bytes as the object may appear as a jumbled mess without this step; or worse it'll be invisible.

With this in mind I'll provide details below on the specifics of object modifications

## Finding a Memory Location for an Object ##
- TODO

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

## Editing Tiles to use for making a new look ##
 - TODO


## Removing Objects for less in the level ##
 - TODO

## Removing Objects for more in the level ##
 - TODO