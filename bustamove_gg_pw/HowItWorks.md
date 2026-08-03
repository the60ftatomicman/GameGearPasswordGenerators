# Password System Reverse Engineering Notes

## Overview

This document describes the password encoding system discovered through reverse engineering.

The password is a 6-character code that stores:

* Starting level
* Number of lives

The password is structured as three symbol pairs:

```
[1][2] [3][4] [5][6]

Pair A   Pair B   Pair C
Lives    Level    Level
         High     Low
         Nibble   Nibble
```

---

## Symbol Table

The game uses a lookup table at `$211F`.

The important part is the symbol index, not the stored byte value.

| Index | Symbol |
| ----- | ------ |
| 0     | B      |
| 1     | C      |
| 2     | D      |
| 3     | F      |
| 4     | G      |
| 5     | H      |
| 6     | J      |
| 7     | K      |
| 8     | L      |
| 9     | M      |
| 10    | N      |
| 11    | P      |
| 12    | Q      |
| 13    | R      |
| 14    | S      |
| 15    | T      |
| 16    | V      |
| 17    | W      |
| 18    | X      |
| 19    | Z      |
| 20    | 0      |
| 21    | 2      |
| 22    | 3      |
| 23    | 4      |
| 24    | 5      |
| 25    | 6      |
| 26    | 7      |
| 27    | 9      |
| 28    | #      |
| 29    | $      |
| 30    | !      |
| 31    | ?      |

---

## Decoding

Each password pair must contain two symbols that resolve to the same value.

The game calculates:

```
Pair A value = symbol_index & $07
Pair B value = symbol_index & $07
Pair C value = symbol_index & $0F
```

The resulting data is:

```
Lives = Pair A value

Level = ((Pair B value << 4) | Pair C value) + 1
```

The level value stored internally is zero based.

Examples:

```
Stored $33 = 51 decimal
Displayed level = 52
```

---

## Symbol Groups

### Lives / Pair A

| Value | Symbols |
| ----- | ------- |
| 0     | B L V 5 |
| 1     | C M W 6 |
| 2     | D N X 7 |
| 3     | F P Z 9 |
| 4     | G Q #   |
| 5     | H R $   |
| 6     | J S !   |
| 7     | K T ?   |

---

### Level High Nibble / Pair B

Same grouping as above, using only values 0-7.

---

### Level Low Nibble / Pair C

| Value | Symbols |
| ----- | ------- |
| 0     | B V     |
| 1     | C W     |
| 2     | D X     |
| 3     | F Z     |
| 4     | G 0     |
| 5     | H 2     |
| 6     | J 3     |
| 7     | K 4     |
| 8     | L 5     |
| 9     | M 6     |
| A     | N 7     |
| B     | P 9     |
| C     | Q #     |
| D     | R $     |
| E     | S !     |
| F     | T ?     |

---

## Example Passwords

### Level 3, 3 Lives

```
FFBBDD
```

Calculation:

```
Lives:
F = index 3
3 lives

Level:
B = 0
D = 2

Level value:
$02 + 1 = 3
```

---

### Level 65, 6 Lives

```
JJGGBB
```

Calculation:

```
Lives:
J = index 6
6 lives

Level:
G = 4
B = 0

Level value:
$40 + 1 = 65
```

---

## Password Generator

The Python script generates valid passwords by:

1. Converting the desired level to zero-based.
2. Splitting the level into high/low nibbles.
3. Selecting matching symbol pairs.
4. Returning a valid six-character password.
