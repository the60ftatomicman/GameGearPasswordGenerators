# Sonic Chaos Offsets Doc #
## Level Headers ##
| Zone | GG Offset | SMS Offset | Bytes |
| :--- | :--- | :--- | :--- |
| **THZ1** | 0 | 0 | 0 |
| **THZ2** | 0 | 0 | 0 |
| **THZ3** | 0 | 0 | 0 |
| | | | |
| **GPZ1** | 0 | 0 | 0 |
| **GPZ2** | 0 | 0 | 0 |
| **GPZ3** | 0 | 0 | 0 |
| | | | |
| **SEZ1** | 0 | 0 | 0 |
| **SEZ2** | 0 | 0 | 0 |
| **SEZ3** | 0 | 0 | 0 |
| | | | |
| **MGHZ1**| 0 | 0 | 0 |
| **MGHZ2**| 0 | 0 | 0 |
| **MGHZ3**| 0 | 0 | 0 |
| | | | |
| **APZ1** | 0 | 0 | 0 |
| **APZ2** | 0 | 0 | 0 |
| **APZ3** | 0 | 0 | 0 |
| | | | |
| **EEZ1** | 0 | 0 | 0 |
| **EEZ2** | 0 | 0 | 0 |
| **EEZ3** | 0 | 0 | 0 |
| | | | |
| **SS1**  | 0 | 0 | 0 |
| **SS2**  | 0 | 0 | 0 |
| **SS3**  | 0 | 0 | 0 |
| **SS4**  | 0 | 0 | 0 |
| **SS5**  | 0 | 0 | 0 |


## level layout offsets ##
| Zone | GG Offset | SMS Offset | Diff Hex | Diff byte | Level Width | Level Height | Tile Offset | Verified in Aspect |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **THZ1** | 48000 | 48000 | 0  | 0  | 128 | 32 | 192 | yes |
| **THZ2** | 48BA9 | 48BA9 | 0  | 0  | 128 | 32 | 192 | yes |
| **THZ3** | 4982C | 49815 | 17 | 23 |  80 | 16 | 192 | yes |
| | | | | | | | | |
| **GPZ1** | 49C3B | 49C25 | 16 | 22 | 160 | 24 | 192 | yes |
| **GPZ2** | 4AA16 | 4AA00 | 16 | 22 | 128 | 32 | 192 | yes |
| **GPZ3** | 4B8AD | 4B897 | 16 | 22 |  80 | 16 | 192 | yes |
| | | | | | | | | |
| **SEZ1** | 54000 | 54000 | 0 | 0 | 128 | 32 | 192 | yes |
| **SEZ2** | 54CC8 | 54CC8 | 0 | 0 | 128 | 32 | 192 | yes |
| **SEZ3** | 53460 | 53460 | 0 | 0 | 128 | 32 | 192 | yes |
| | | | | | | | | |
| **MGHZ1**| 559D4 | 559D4 | 0 | 0 | 128 | 32 | 192 | yes |
| **MGHZ2**| 566B8 | 566B8 | 0 | 0 | 128 | 32 | 192 | yes |
| **MGHZ3**| 572FB | 572FB | 0 | 0 | 120 | 24 | 192 | yes |
| | | | | | | | | |
| **APZ1** | 5C000 | 5C000 |  0  |  0  | 168 | 24 | 192 | yes |
| **APZ2** | 5C7C1 | 5C7C1 |  0  |  0  | 128 | 32 | 192 | yes |
| **APZ3** | 578A6 | 57AF3 | 24D | 589 |  80 | 16 | 192 | yes |
| | | | | | | | | |
| **EEZ1** | 5CF3A | 5CF3A | 0 | 0 | 128 | 32 | 192 | yes |
| **EEZ2** | 5DB73 | 5DB73 | 0 | 0 | 128 | 32 | 192 | yes |
| **EEZ3** | 5E853 | 5E853 | 0 | 0 | 112 | 32 | 192 | yes |
| | | | | | | | | |
| **SS1**  | 68000 | 68000 | 0 | 0 | 512 |  8 | 192 | yes |
| **SS2**  | 685A8 | 685A8 | 0 | 0 |  24 | 64 | 192 | yes but omg these values are wrong....|
| **SS3**  | 68819 | 68848 | | | 128 | 24 | 192 | yes |
| **SS4**  | 68BEF | 68C1E | | | 256 | 16 | 192 | yes |
| **SS5**  | 69220 | 69258 | | |  48 | 32 | 192 | yes |

## mappings offset ##

 _LABEL_1024_ (in emulicious you can set a BP here and see the mappings load! via AF register, remember to flip to FA)

| Zone | GG Offset | SMS Offset | Diff Hex | Diff byte | Verified in Aspect |
| :--- | :--- | :--- | :--- | :--- | :--- |
| THZ     | 44000 | 44000 | 0 | 0 | yes |
| GPZ     | 45640 | 45640 | 0 | 0 | yes |
| SEZ     | 46A40 | 46A40 | 0 | 0 | yes |
| MGHZ    | 50000 | 50000 | 0 | 0 | yes |
| APZ     | 51320 | 51320 | 0 | 0 | yes |
| EEZ     | 524E0 | 524E0 | 0 | 0 | yes |
| SS1/2/4 | 6C000 | 6C000 | 0 | 0 | yes |
| SS3/5   | 6CF60 | 6CF60 | 0 | 0 | yes |

## tileset offset ##
| Zone | GG Offset | SMS Offset | Diff Hex | Diff byte | Verified in Aspect |
| :--- | :--- | :--- | :--- | :--- | :--- |
| THZ     | 40A70 | 40F9E |  0  | 0    | yes |
| GPZ     | 41F4A | 42478 |  0  |  0   | yes |
| SEZ     | 60840 | 60000 | 840 | 2112 | yes |
| MGHZ    | 62230 | 619F0 |  0  |  0   | yes |
| APZ     | 58000 | 58000 |  0  |  0   | yes |
| EEZ     | 59800 | 59800 |  0  |  0   | yes |
| SS1/2/4 | 64000 | 64000 |  0  |  0   | yes |
| SS3/5   | 65590 | 65590 |  0  |  0   | yes |
 
 
 you found palettes in emulicious by getting to the level and just searching for the string values!
 memory editor -> palettes. First 2 rows are for foreground, second two rows for background
 
## foreground palette offset ## 
| Zone | GG Offset | SMS Offset | Diff Hex | Diff byte | Verified in Aspect |
| :--- | :--- | :--- | :--- | :--- | :--- |
| THZ     | 3B8F3 | 3B6AD | | | yes |
| GPZ     | 3B913 | 3B6BD | | | yes |
| SEZ     | 3B933 | 3B6CD | | | yes |
| MGHZ    | not found? | 3B6DD | | | |
| APZ     | 3B973 | 3B6ED | | | yes |
| EEZ     | 3B993 | 3B6FD | | | yes |
| SS1/2/4 | 3BB13 | 3B76D | | | yes |
| SS3     | | 3B77D | | | |
| SS5     | | 3B78D | | | |

## background palette offset ## 
| Zone | GG Offset | SMS Offset | Diff Hex | Diff byte | Verified in Aspect |
| :--- | :--- | :--- | :--- | :--- | :--- |
| THZ     | 3B713          | 3B79D | | | yes |
| GPZ     | 3B730 or 3B7B3 | 3B7AD | | | |
| SEZ     | 3B753          | 3B7BD | | | yes |
| MGHZ    | 3B773          | 3B7CD | | | yes |
| APZ     | 3B793          | 3B7DD | | | yes |
| EEZ     | 3B733 or 3B7B3 | 3B7ED | | | |
| SS1/2/4 | 3B893          | 3B8AD | | | yes |
| SS3     | | 3B8BD | | | |
| SS5     | | 3B8BD | | | |