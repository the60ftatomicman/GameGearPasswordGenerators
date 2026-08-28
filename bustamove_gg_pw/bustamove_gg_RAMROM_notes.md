RAM:C105 = level index (confirmed)

_DATA_392B_ == background table.
00 == Granite blocks
01 == Starry sky
02 == Bubbles
03 == Cave
04 == Trees / Forest
05 == Stained Glass / Cathedral
06 ==  purple planet / cityscape?
07 == Ocean
08 == Egyptian ruins
09 == between two trees
0A == Flower field
0B == Inside barn with candles
0C == palatial steps
0D == Clocks
OE == Gears and Chains
OF == roses (Challenge Mode)
10 or greater == broken

# How graphics and ball data are stored #
everything from $A9 - $FF in the VDP are where we store the actual live layout of the map. These are dynamically created

_LABEL_31A_  - clears level

RAM D040 --- here is where we point the HL to outi and load our ball data

Who writes to d040?
a ton! but _LABEL_4C02 looks like it loads it with the data we WANT
TWIST! C400 == our true UNFILTERED ram location for the level layout. C4xx byte rows use the 15 bytes of the row to represent a level row. the 16th byte is skipped.
The index of the balls below do NOT map to the palette colors directly. but rather the tiles in the sprite index.
00 = empty
01 = black
02 = red
03 = yellow
04 = green
05 = purple
06 = orange
07 = blue
08 = light grey
09 = green again
0A = fire
0B = water
OC = lightening
OD = pop animation 1
0E = pop animation 2
OF = some gem looking one that never pops


_LABEL_43D2_ == we write the spheres out to c400 here.
we do so on the line under the call to _LABEL_44D2_.

We move the DE pointer to _RAM_C400_ under _LABEL_43AC_ so presummably this is important.


SHAZAM!
the _LABEL_43D2_ label is the importabt one. above all of the RRCA calls, we load the balls 2 at a time. High and low nibble == first than second ball.

9598 --- first ball I see loaded. is it 22? can I adjust it to say... 33?

YES!!!! AT 0F:959B we we see level one. it will load until it sees...FF!
All levels defined this way. 
THIS IS THE ANSWER!!!



_LABEL_427_ = we dynamically set the VDP tile
    -> _LABEL_81B_  = label before 427
    -> _LABEL_4CCF_ = label before 81B
    -> _LABEL_47C9_ = label before 4ccF
        -> here we have a ton of aRAM checks
        -> the _RAM_D40_ spot doesn't control ball type